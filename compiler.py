import docker
from language import SUPPORT_LANGUAGE
import settings
import time
import os
import sys

docker_repo_arguments = '{CDN_HUB}/{lang}:{tag}'
source_file_name = 'main-{thread}.{extension}'
client = docker.from_env()

def create_tempfile( thread_id , lang , code ):
    if lang not in SUPPORT_LANGUAGE:
        return 'Unsupported Language'
    try:
        f = open( 'work/' + source_file_name.format(
            thread = thread_id,
            extension = SUPPORT_LANGUAGE[lang]['extension']
        )   
        , 'w' )
        f.write( code )
    except:
        return 'Judger Error'
    return 'Success' , 'main-' + str( thread_id )

def Compile( lang , code , sourcefile ):
    sourcefile_withextension = sourcefile + '.' + SUPPORT_LANGUAGE[lang]['extension']
    try:
        s = client.containers.create(
            image = docker_repo_arguments.format(
                CDN_HUB = settings.CDN_HUB_ADDRESS,
                lang = SUPPORT_LANGUAGE[lang]['docker_repo'],
                tag = SUPPORT_LANGUAGE[lang]['docker_repo_tag'],
                mem_limit = settings.COMPILE_MEMORY,
            ),
            volumes={ os.path.join( settings.work_dir , sourcefile_withextension ) : {'bind': os.path.join( '/opt' , sourcefile_withextension ) , 'mode':'ro' } },
            working_dir = '/opt',
            command = SUPPORT_LANGUAGE[lang]['compile_command'].format(
                compile_timeout = settings.COMPILE_TIMEOUT,
                source_file = sourcefile,
                extension = SUPPORT_LANGUAGE[lang]['extension'],
            ),
            auto_remove = False,
        )
        s.start()
        s.wait()
        print( 'Run Complete' )
    except docker.errors.ContainerError as e:
        compile_info_msg = e.stderr.decode('utf-8')[:min( len(e.stderr) , settings.max_compile_error_length )]
        return 'Compile Error' , compile_info_msg
    except:
        return 'Compile Error' , 'Unknown Error'
    finally:
        print(s.logs())
        s.remove( force = True )
    return 'Success' , None

if __name__ == '__main__':
    s1 = time.clock()
    #print( create_tempfile( 1 , 'GNU G++17' , '#include <iostream>' ) )
    print( Compile( 'GNU G++17' , 'main' , 'main-1' )[1] )
    print( 'time cost ' , time.clock() - s1 )
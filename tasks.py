from celery import Celery
from celeryconfig import broker
from billiard import Semaphore, Process, current_process
from settings import MAX_JUDGE_PROCESS, base_work_dir
from judger import judge_submission
from submission.models import Submission, parse
from os import path


app = Celery(
    name = 'task',
    broker = broker
)

sep = Semaphore( MAX_JUDGE_PROCESS )

def JudgingProcess( submission ):
    main , _suff = current_process().name.split( ':' )
    _suff = int( _suff ) % MAX_JUDGE_PROCESS
    name = 'Process-' + str( _suff )
    try:
        submission = parse( ** submission )
        sub = Submission( ** { ** submission , ** {
            'work_dir' : path.join( base_work_dir , name ),
            'output_limit' : 64,
            'stack_limit' : 64,
            'sourcefile': 'main' }})
        print( name , 'got submission, start juding(%s)' % ( str( sub.submission ) )  )
        judge_submission( sub )
    except Exception as e:
        print( name , 'error happen:' , str( e ) )
    finally:
        sep.release()

@app.task( name = 'Judger.task' )
def Submission_task( submission ):
    sep.acquire()
    Process( target = JudgingProcess , args = ( submission , ) , daemon = True ).start()
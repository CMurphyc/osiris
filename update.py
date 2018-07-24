from requests import post
from settings import RESULT_QUEUE
import logging


def upload_result(report):
    '''
        Send the report to the server
    '''
    report.result = report.result.value.full
    logging.info(report.attribute)
    from tasks import upload_result_into_queue
    upload_result_into_queue.apply_async(
        args=(report.attribute, ), queue=RESULT_QUEUE)

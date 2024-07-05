import allure
from allure_commons.types import AttachmentType


def add_logs_request(result):
    allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                  extension="txt")
    allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.JSON, extension="txt")
    allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

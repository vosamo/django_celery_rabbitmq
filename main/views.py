from time import sleep
from main.tasks import ground_work
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult
class Hello(APIView):
    """
    Request produce a task.
    """
    def get(self, request):
        res = ground_work.delay()               # Allocate a task to a worker.
        result = 'Task id is:%s' % res.id          # Each task has a unique id.
        return Response(result, status=status.HTTP_200_OK)

class TaskState(APIView):
    def get(self, request, uuid):
        res = AsyncResult(uuid)                 # Reconstruct a AsyncResult object with task id.
        if res.ready():                         # Judge whether the task is finished,if result is ready,get it with get() method.
            task_res = res.get()                # Get task result.
        else:
            task_res = "Task not finished!"
        return Response(task_res, status=status.HTTP_200_OK)



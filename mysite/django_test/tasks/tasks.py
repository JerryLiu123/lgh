from celery.decorators import task


@task
def test(x, y):
    return x + y

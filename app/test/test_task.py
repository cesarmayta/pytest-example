import pytest

from datetime import datetime
from datetime import timedelta

from app.task import Task,DueDateError

def is_available_to_skip():
    return True

@pytest.fixture
def username():
    return 'cesar'

def test_username(username):
    assert username == 'cesar'

class TestTask():
    
    def test_task(self):
        assert True
    
    @pytest.mark.new
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('title','description','cesar',due_date)
        
        assert task.title == 'title'
        assert task.description == 'description'
        assert task.assigned_to == 'cesar'
        assert task.due_date == due_date
        
    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=2)
            Task('title','description','cesar',due_date)
        
    @pytest.mark.due_date    
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('title','description','cesar',due_date)
        
        assert task.due_date > datetime.now()
        
    # para saltar pruebas
    # skip
    # skipif
    
    
    
    @pytest.mark.skip(reason='lo sentimos, la prueba no cumple con los requerimientos')
    def test_skip(self):
        pass
    
    @pytest.mark.skipif(is_available_to_skip,reason='lo sentimos, la prueba no cumple con los requerimientos')
    def test_skip_if(self):
        pass
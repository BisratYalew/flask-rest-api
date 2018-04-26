import json

from flask_rest_api import db
from flask_rest_api.application import create_app

## Module to make a unit test
from unittest import TestCase


class TestView(TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.client = self.app.test_client()
        db.create_all(app=self.app)

    def test_create_company(self):
        data = dict(name='test', country_code='ET', website='http://example.com', enabled=True)
        response = self.client.post('/companies', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 200

    def test_delete_company(self):
        data = dict(name='test', country_code='ET', website='http://example.com', enabled=True)
        response = self.client.post('/companies', data=json.dumps(data), content_type='application/json')

        company = json.loads(response.get_data(as_text=True))

        response = self.client.delete('/companies/' + str(company.get('id')))
        assert response.status_code == 204


    def get_company(self):
        data = dict(name='test', country_code='ET', website='http://example.com', enabled=True)
        response = self.client.post('/companies', data=json.dumps(data), content_type='application/json')
        company = json.loads(response.get_data(as_text=True))

        response = self.client.get('/companies/' + str(company.get('id')))

        assert response.status_code == 200

        company = json.loads(response.get_data(as_text=True))

        assert company.get('name') == 'test'

 
    def list_companies(self):
        data = dict(name='test', country_code='ET', website='http://example.com', enabled=True)
        self.client.post('/companies', data=json.dumps(data), content_type='application/json')

        response = self.client.get('/companies')

        assert response.status_code == 200

        companies = json.loads(response.get_data(as_text=True))

        assert len(companies) == 1

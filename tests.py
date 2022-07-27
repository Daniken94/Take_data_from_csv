import pytest

from app import FetchStudentDetails
from student import Student


class TestGetData:
    def test_record_count(self):
        fetch_student = FetchStudentDetails()
        result = fetch_student.get_data()
        assert len(result) == 6

    def test_clean_headers(self):
        fetch_student = FetchStudentDetails()
        fetch_student.get_data()
        headers = fetch_student.headers
        assert len(headers) == 6

    def test_age_integer(self):
        fetch_student = FetchStudentDetails()
        result = fetch_student.get_data()
        assert result[0].age == 17

    def test_avg_score_sum(self):
        fetch_student = FetchStudentDetails()
        result = fetch_student.get_data()
        avg_score_sum = sum(r.average_score for r in result)
        assert avg_score_sum == 498.3

class TestSuperStudent:
    def test_get_super_student(self):
        fetch_student = FetchStudentDetails()
        fetch_student.get_data()
        super_student = fetch_student.get_super_student()

        assert type(super_student) == Student
        assert super_student.name == "yohan doe"
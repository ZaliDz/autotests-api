from http import HTTPStatus

import pytest
from fixtures.courses import CourseFixture
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExercisesResponseSchema, UpdateExerciseRequestSchema, \
UpdateExerciseResponseSchema, GetExerciseQuerySchema, GetExerciseResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, assert_update_exercise_response, \
assert_exercise_not_found_response, assert_get_exercises_response
from fixtures.exercises import ExerciseFixture
from clients.errors_schema import InternalErrorResponseSchema



@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:

    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
        
    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercises: ExerciseFixture):

        response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercises.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercises: ExerciseFixture):

        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercises.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)
        
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)
        
        validate_json_schema(response.json(), response_data.model_json_schema())


    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercises: ExerciseFixture):

        delete_response = exercises_client.delete_exercise_api(function_exercises.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        response_data = InternalErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_exercises: ExerciseFixture,
            function_course: CourseFixture
    ):
        create_response = exercises_client.create_exercise(function_exercises.request)
        query = GetExerciseQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercises.response])

        validate_json_schema(response.json(), response_data.model_json_schema())


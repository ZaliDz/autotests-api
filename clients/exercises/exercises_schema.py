from pydantic import BaseModel, Field, ConfigDict


class Exercise(BaseModel):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: Exercise

class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")

class UpdateExerciseRequestSchema(BaseModel):
    '''
    Описание структуры запроса обновления упражнения
    '''
    title: str = Field(default=None)
    course_id: str = Field(default=None, alias="courseId")
    max_score: int = Field(default=None, alias="maxScore")
    min_score: int = Field(default=None, alias="minScore")
    order_index: int = Field(default=None, alias="orderIndex")
    description: str = Field(default=None)
    estimated_time: str = Field(default=None, alias="estimatedTime")

class CreateExerciseRequestSchema(BaseModel):
    '''
    Описание структуры запроса обновления упражнения
    '''
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    '''
    Описание структуры ответа создания упражнения
    '''
    exercise: Exercise

class UpdateExerciseResponseSchema(BaseModel):
    '''
    Описание структуры ответа обновления упражнения
    '''
    exercise: Exercise

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercise: list[Exercise]

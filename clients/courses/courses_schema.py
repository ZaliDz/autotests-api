from pydantic import BaseModel, Field, ConfigDict
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    '''
    Описание структуры создания курса
    '''

    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file_id: str = Field(alias="previewFileId")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user_id: str = Field(alias="createdByUserId")


class Course(BaseModel):

    '''Описание структуры курса'''
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")

class CreateCourseResponseSchema(BaseModel):
    '''
    Описание структуры ответа создания курса
    '''

    model_config = ConfigDict(populate_by_name=True)

    courses: Course
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class GetCoursesResponseSchema(BaseModel):
    '''Описание структуры ответа получения информация о курсах'''

    courses: list[CreateCourseResponseSchema]


class UpdateCourseRequestSchema(BaseModel):
    '''Описание структуры обновления информации о курсе'''

    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default=None)
    max_score: int = Field(alias="maxScore", default=None)
    min_score: int = Field(alias="minScore",default=None)
    description: str = Field(default=None)
    estimated_time: str = Field(alias="estimatedTime",default=None)

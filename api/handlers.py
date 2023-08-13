from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import UserCreate, ShowUser
from db.dals import UserDAL
from db.session import get_db

user_router = APIRouter()

"""Аналог views и url в django"""


async def _create_new_user(body: UserCreate, db) -> ShowUser:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email,
            )
            return ShowUser(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=user.email,
                is_active=user.is_active,
            )


async def _delete_user(user_id, db) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            deleted_user_id = await user_dal.delete_user(
                user_id=user_id,
            )
            return deleted_user_id


async def _update_user(updated_user_params: dict, user_id: UUID, db) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            updated_user_id = await user_dal.update_user(
                user_id=user_id,
                **updated_user_params
            )
            return updated_user_id


async def _get_user_by_id(user_id, db) -> Union[ShowUser, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_id(
                user_id=user_id,
            )
            if user is not None:
                return ShowUser(
                    user_id=user.user_id,
                    name=user.name,
                    surname=user.surname,
                    email=user.email,
                    is_active=user.is_active,
                )


@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    """
    Так как в Depends была передана функция-генератор get_db, то сначала будет вызвана эта функция, затем получена
    сессия из yields и передана в качестве параметра db в функцию create_new_user.
    И уже после выполнения _create_new_user генератор get_db завершит свою работу и выполнит код после yields.
    В нашем случае закроет сессию.
    """
    return await _create_new_user(body, db)

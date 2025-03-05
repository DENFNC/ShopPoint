from typing import Annotated
from typing import List
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession


from app.backend import get_session
from app.service import create_role_service
from app.service import get_roles_service
from app.service import get_role_service
from app.schemas import CreateRole
from app.schemas import RoleInDB


router = APIRouter(prefix='/api/v1/auth', tags=['Role'])


@router.get('/roles', response_model=List[RoleInDB])
async def get_roles(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    result = await get_roles_service(
        db=db
    )

    return result


@router.get('/roles/{role_id}', response_model=RoleInDB)
async def get_role(
    db: Annotated[AsyncSession, Depends(get_session)],
    role_id: int
):
    result = await get_role_service(
        db=db,
        role_id=role_id
    )

    return result


@router.post('/roles', status_code=status.HTTP_201_CREATED)
async def create_role(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_role: CreateRole
):
    await create_role_service(
        db=db,
        create_role=create_role
    )

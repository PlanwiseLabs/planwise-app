from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_tasks():
    """Return a list of tasks (placeholder)."""
    return []


@router.post("")
async def create_task(task: dict):
    """Create a new task (placeholder)."""
    return task

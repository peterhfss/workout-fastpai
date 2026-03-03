from .athlete_repository import AthleteRepository
import pytest

@pytest.mark.asyncio
@pytest.mark.skip(reason="Skipping insert athlete  in the database")
async def test_add_athlete():
    new_athlete = {
        "name": "John Doe",
        "cpf": "1234567",
        "age": 20,
        "height": 1.80,
        "weight": 70,
        "gender": "male"
    }
    
    repo = AthleteRepository()
    await repo.add_athlete(new_athlete)
    
    

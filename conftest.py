import pytest
import pypuppetdb


# Set up our API objects
@pytest.fixture
def baseapi():
    return pypuppetdb.api.BaseAPI()


@pytest.fixture
def utc():
    """Create a UTC object."""
    return pypuppetdb.utils.UTC()

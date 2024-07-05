import pytest
from framework_for_api_tests.items import BOOK_ID

add_item_positive_post = [
    pytest.param(
        {
            "id": BOOK_ID,
            "adData": {
                "item_list_name": "index",
                "product_shelf": "Новинки литературы"
            }
        },
        200,
        marks=pytest.mark.positive,
    ),
]

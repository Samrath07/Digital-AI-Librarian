import httpx
import os
from fastapi import HTTPException
from app.schemas.book_schema import BookResponse

GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")
GOOGLE_BOOKS_URL = os.getenv("BOOKS_URL")

async def fetch_books_from_google(query: str) -> list[dict]:
    params = {
        "q": query,
        "key": GOOGLE_BOOKS_API_KEY,
        "maxResults": 10
    }
    async with httpx.AsyncClient(timeout=10) as client:

        try:
            response = await client.get(GOOGLE_BOOKS_URL, params=params)
            response.raise_for_status()
            data = response.json()
            data = data["items"] if "items" in data else []
            data_response = build_google_response(data)
            return data_response
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail=e)


def build_google_response(data: list[dict]) -> list[BookResponse]:

    response = []

    for item in data:

        volume_info = item.get("volumeInfo", {})
        sale_info = item.get("saleInfo", {})

        isbn_10 = None
        isbn_13 = None

        for identifier in volume_info.get("industryIdentifiers", []):

            if identifier.get("type") == "ISBN_10":
                isbn_10 = identifier.get("identifier")

            elif identifier.get("type") == "ISBN_13":
                isbn_13 = identifier.get("identifier")

        book = BookResponse(
            google_book_id=item.get("id"),
            title=volume_info.get("title", "Unknown Title"),
            description=volume_info.get("description", "No description available"),
            isbn_13=isbn_13,
            isbn_10=isbn_10,
            price=sale_info.get("listPrice", {}).get("amount"),
            category=volume_info.get("categories", []),
            authors=volume_info.get("authors", []),
            publisher=volume_info.get("publisher", "Unknown Publisher"),
            published_date=volume_info.get("publishedDate", "Unknown Date"),
            pages=volume_info.get("pageCount", 0),
        )

        response.append(book)

    return response
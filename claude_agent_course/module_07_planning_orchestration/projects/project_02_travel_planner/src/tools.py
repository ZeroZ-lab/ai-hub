def search_flights(origin: str, destination: str, date: str) -> str:
    """查询航班"""
    return f"Flight Found: {origin} -> {destination} on {date}, Price: $500, Airline: AirAI"

def search_hotels(location: str, date: str) -> str:
    """查询酒店"""
    return f"Hotel Found: Grand AI Hotel at {location}, Date: {date}, Price: $150/night"

def book_ticket(flight_info: str) -> str:
    """预订机票"""
    return f"Confirmed: Ticket booked for {flight_info}. Confirmation Code: XYZ123"

def book_hotel(hotel_info: str) -> str:
    """预订酒店"""
    return f"Confirmed: Hotel booked for {hotel_info}. Confirmation Code: HTL456"

TOOLS_MAP = {
    "search_flights": search_flights,
    "search_hotels": search_hotels,
    "book_ticket": book_ticket,
    "book_hotel": book_hotel
}

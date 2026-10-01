"""
FINN MCP Server — search, price stats, and account management.
Combines finn_api (REST search) with FinnBrowser (Playwright account actions).
"""
import json
from typing import Any, Optional

from fastmcp import FastMCP

from finn_api import FinnAPI

mcp = FastMCP("finn-market")
api = FinnAPI()


# ═══════════════════════════════════════════
# Search tools (existing)
# ═══════════════════════════════════════════

@mcp.tool()
def search(
    query: Optional[str] = None,
    rows: int = 50,
    page: int = 1,
    published_today: Optional[bool] = None,
    sort: Optional[str] = None,
    fiks_ferdig: Optional[bool] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
) -> dict:
    """Search FINN marketplace listings.
    
    Args:
        query: Search terms
        rows: Results per page (max 50)
        page: Page number for pagination
        fiks_ferdig: Only show listings available through Fiks ferdig
        min_price: Minimum price in NOK
        max_price: Maximum price in NOK
        published_today: Only show listings published today
        sort: Sort order — "PRICE_ASC" for low-to-high, "PRICE_DESC" for high-to-low
    """
    results = api.search(
        query=query,
        rows=rows,
        page=page,
        published_today=published_today,
        sort=sort,
        fiks_ferdig=fiks_ferdig,
        min_price=min_price,
        max_price=max_price,
    )
    return {"results": results}


@mcp.tool()
def get_urls(ids: list[str]) -> dict:
    """Get the URLs for multiple FINN listings based on their IDs."""
    urls = [api.get_url(id) for id in ids]
    return {"urls": urls}


@mcp.tool()
def get_info(ids: list[str]) -> dict:
    """Fetch listing description and location for multiple or singular FINN listings."""
    info = api.get_info(ids)
    return {"info": info}

if __name__ == "__main__":
    mcp.run()

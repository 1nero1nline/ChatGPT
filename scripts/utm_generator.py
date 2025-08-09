#!/usr/bin/env python3
"""
UTM Generator

This script helps you quickly generate UTM-tagged URLs for marketing campaigns.
"""

from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl


def generate_utm_url(base_url, source, medium, campaign, content=None, term=None):
    """Generate a URL with UTM parameters appended.

    Args:
        base_url (str): The original URL without UTM parameters.
        source (str): utm_source, e.g. 'newsletter', 'facebook', 'google'.
        medium (str): utm_medium, e.g. 'email', 'cpc', 'social'.
        campaign (str): utm_campaign name or identifier.
        content (str, optional): utm_content to differentiate ads. Defaults to None.
        term (str, optional): utm_term for paid search keywords. Defaults to None.

    Returns:
        str: The URL with UTM parameters appended.
    """
    # Parse existing query parameters
    parsed_url = urlparse(base_url)
    query_params = dict(parse_qsl(parsed_url.query))

    # Define new UTM parameters
    utm_params = {
        "utm_source": source,
        "utm_medium": medium,
        "utm_campaign": campaign,
    }
    if content:
        utm_params["utm_content"] = content
    if term:
        utm_params["utm_term"] = term

    # Merge and build new query string
    query_params.update(utm_params)
    new_query = urlencode(query_params)

    # Construct and return the new URL
    return urlunparse(parsed_url._replace(query=new_query))


if __name__ == "__main__":
    # Example usage: generate a UTM-tagged URL and print it
    url = generate_utm_url(
        base_url="https://example.com/landing",
        source="newsletter",
        medium="email",
        campaign="summer_sale",
        content="banner1"
    )
    print(url)

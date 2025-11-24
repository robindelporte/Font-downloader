#!/usr/bin/env python3
"""
Google Fonts WOFF2 Downloader
Downloads Google Fonts in WOFF2 format from a Google Fonts URL
"""

import re
import sys
import argparse
import urllib.request
import urllib.parse
from pathlib import Path


def extract_font_family(url_or_name):
    """Extract font family name from Google Fonts URL or return the name directly."""
    if url_or_name.startswith('http'):
        # Parse Google Fonts URL
        # Example: https://fonts.google.com/specimen/Roboto
        # or: https://fonts.googleapis.com/css2?family=Roboto:wght@400;700

        if 'googleapis.com' in url_or_name:
            # Extract from CSS API URL
            match = re.search(r'family=([^:&]+)', url_or_name)
            if match:
                return urllib.parse.unquote(match.group(1))
        elif 'fonts.google.com' in url_or_name:
            # Extract from specimen URL
            match = re.search(r'/specimen/([^/?]+)', url_or_name)
            if match:
                return urllib.parse.unquote(match.group(1))

        raise ValueError("Unable to extract font family from URL")
    else:
        # Assume it's a font family name
        return url_or_name


def build_google_fonts_url(font_family):
    """Build a Google Fonts CSS URL with common weights."""
    # Replace spaces with +
    family_param = font_family.replace(' ', '+')
    # Request common weights and styles
    return f'https://fonts.googleapis.com/css2?family={family_param}:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap'


def fetch_css(url):
    """Fetch the CSS file from Google Fonts with WOFF2 user agent."""
    # Use a modern browser user agent to get WOFF2 format
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/css,*/*;q=0.1',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://fonts.googleapis.com/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'style',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin'
    }

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')


def extract_woff2_urls(css_content):
    """Extract WOFF2 font URLs from the CSS content."""
    # Match url(https://...woff2) patterns
    pattern = r'url\((https://[^)]+\.woff2)\)'
    urls = re.findall(pattern, css_content)
    return urls


def sanitize_filename(url):
    """Create a safe filename from the font URL."""
    # Extract the last part of the URL path
    filename = url.split('/')[-1]
    # Remove query parameters if any
    filename = filename.split('?')[0]
    return filename


def download_font(url, output_dir):
    """Download a single WOFF2 font file."""
    output_path = output_dir / sanitize_filename(url)

    # Skip if already downloaded
    if output_path.exists():
        print(f"  ⏭️  Already exists: {output_path.name}")
        return output_path

    try:
        print(f"  ⬇️  Downloading: {output_path.name}")

        # Add headers for font download
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'https://fonts.googleapis.com/'
        }

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(output_path, 'wb') as f:
                f.write(response.read())

        return output_path
    except Exception as e:
        print(f"  ❌ Failed to download {url}: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Download Google Fonts in WOFF2 format',
        epilog='Examples:\n'
               '  %(prog)s "Roboto"\n'
               '  %(prog)s "https://fonts.google.com/specimen/Roboto"\n'
               '  %(prog)s "https://fonts.googleapis.com/css2?family=Roboto" -o my-fonts',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('font', help='Google Fonts URL or font family name')
    parser.add_argument('-o', '--output', default='fonts',
                       help='Output directory for downloaded fonts (default: fonts)')

    args = parser.parse_args()

    try:
        # Extract font family name
        print(f"🔍 Extracting font family...")
        font_family = extract_font_family(args.font)
        print(f"✅ Font family: {font_family}")

        # Build Google Fonts URL
        css_url = build_google_fonts_url(font_family)
        print(f"\n📥 Fetching font data from Google Fonts...")

        # Fetch CSS
        css_content = fetch_css(css_url)

        # Extract WOFF2 URLs
        woff2_urls = extract_woff2_urls(css_content)

        if not woff2_urls:
            print("❌ No WOFF2 fonts found. The font might not be available.")
            return 1

        print(f"✅ Found {len(woff2_urls)} WOFF2 font file(s)")

        # Create output directory
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n📁 Saving fonts to: {output_dir.absolute()}")

        # Download fonts
        print(f"\n⬇️  Downloading fonts...")
        downloaded = []
        for url in woff2_urls:
            result = download_font(url, output_dir)
            if result:
                downloaded.append(result)

        # Summary
        print(f"\n✅ Successfully downloaded {len(downloaded)} font file(s)!")
        print(f"📂 Location: {output_dir.absolute()}")

        return 0

    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())

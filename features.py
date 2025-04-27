import re
import socket
import urllib
from urllib.parse import urlparse
import requests

def using_ip(url):
    try:
        ip = socket.gethostbyname(urlparse(url).netloc)
        return 1
    except:
        return 0

def long_url(url):
    return 1 if len(url) >= 75 else 0

def short_url(url):
    shortening_services = r"bit\.ly|goo\.gl|tinyurl\.com|ow\.ly|t\.co|bitly\.com|is\.gd|buff\.ly|adf\.ly"
    return 1 if re.search(shortening_services, url) else 0

def has_at_symbol(url):
    return 1 if "@" in url else 0

def has_redirect(url):
    return 1 if "//" in urlparse(url).path else 0

def prefix_suffix(url):
    domain = urlparse(url).netloc
    return 1 if "-" in domain else 0

def sub_domains(url):
    domain = urlparse(url).netloc
    return 1 if domain.count('.') > 2 else 0

def https_token(url):
    return 0 if urlparse(url).scheme == "https" else 1

def domain_registration_length(url):
    # Placeholder: Normally requires WHOIS lookup
    return 0  # 0: Long registration, 1: Short (phishing tendency)

def favicon(url):
    # Placeholder: Needs HTML parsing normally
    return 0

def non_std_port(url):
    parsed = urlparse(url)
    return 1 if parsed.port and parsed.port not in [80, 443] else 0

def https_in_domain(url):
    domain = urlparse(url).netloc
    return 1 if "https" in domain else 0

def request_url(url):
    # Placeholder: Needs checking external resources in HTML
    return 0

def anchor_url(url):
    # Placeholder: Needs anchor tag analysis
    return 0

def links_in_script_tags(url):
    # Placeholder
    return 0

def server_form_handler(url):
    # Placeholder: Needs form action analysis
    return 0

def info_email(url):
    return 1 if "mailto:" in url else 0

def abnormal_url(url):
    return 0  # Placeholder

def website_forwarding(url):
    try:
        r = requests.get(url, timeout=5)
        return 1 if len(r.history) > 2 else 0
    except:
        return 1

def status_bar_customization(url):
    # Placeholder: Requires Javascript inspection
    return 0

def disable_right_click(url):
    # Placeholder
    return 0

def using_popup_window(url):
    # Placeholder
    return 0

def iframe_redirection(url):
    # Placeholder
    return 0

def age_of_domain(url):
    # Placeholder: Requires WHOIS lookup
    return 0

def dns_recording(url):
    try:
        socket.gethostbyname(urlparse(url).netloc)
        return 0
    except:
        return 1

def website_traffic(url):
    # Placeholder: Needs Alexa Rank or similar
    return 0

def page_rank(url):
    # Placeholder
    return 0

def google_index(url):
    query = f"https://www.google.com/search?q=site:{url}"
    try:
        r = requests.get(query, timeout=5)
        return 0 if "did not match any documents" in r.text else 1
    except:
        return 1

def links_pointing_to_page(url):
    # Placeholder
    return 0

def stats_report(url):
    # Placeholder
    return 0

def extract_features(url):
    features = [
        using_ip(url),             # UsingIP
        long_url(url),             # LongURL
        short_url(url),            # ShortURL
        has_at_symbol(url),        # Symbol@
        has_redirect(url),         # Redirecting//
        prefix_suffix(url),        # PrefixSuffix-
        sub_domains(url),          # SubDomains
        https_token(url),          # HTTPS
        domain_registration_length(url),  # DomainRegLen
        favicon(url),              # Favicon
        non_std_port(url),         # NonStdPort
        https_in_domain(url),      # HTTPSDomainURL
        request_url(url),          # RequestURL
        anchor_url(url),           # AnchorURL
        links_in_script_tags(url), # LinksInScriptTags
        server_form_handler(url),  # ServerFormHandler
        info_email(url),           # InfoEmail
        abnormal_url(url),         # AbnormalURL
        website_forwarding(url),   # WebsiteForwarding
        status_bar_customization(url), # StatusBarCust
        disable_right_click(url),  # DisableRightClick
        using_popup_window(url),   # UsingPopupWindow
        iframe_redirection(url),   # IframeRedirection
        age_of_domain(url),        # AgeofDomain
        dns_recording(url),        # DNSRecording
        website_traffic(url),      # WebsiteTraffic
        page_rank(url),            # PageRank
        google_index(url),         # GoogleIndex
        links_pointing_to_page(url),  # LinksPointingToPage
        stats_report(url)          # StatsReport
    ]
    return features

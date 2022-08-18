#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline.ingestion_models import EventIngestionModel
from cdp_scrapers.legistar_utils import LegistarScraper

###############################################################################


def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[EventIngestionModel]:
    scraper = LegistarScraper(
        client="oakland",
        timezone="America/Los_Angeles",
        ignore_minutes_item_patterns=[
            (
                "the City Council has found that an imminent risk to the "
                "health of attendees due to the COVID-19 pandemic continues to exist"
            ),
            (
                "PUBLIC PARTICIPATION The public may observe and/or "
                "participate in this meeting many ways"
            ),
            (
                "Americans With Disabilities Act If you need special assistance "
                "to participate in Oakland City Council"
            ),
            "THE HANGING OF BANNERS, POSTERS, SIGNS, OR ANY MATERIAL",
            (
                "MATERIALS RELATED TO ITEMS ON THIS AGENDA SUBMITTED TO "
                "THE CITY COUNCIL AFTER DISTRIBUTION"
            ),
            "There are three ways to submit public comments",
            (
                "When possible, please notify the City Clerk 5 days prior "
                "to the meeting so we can make reasonable arrangements"
            ),
        ],
    )

    return scraper.get_events(begin=from_dt, end=to_dt)

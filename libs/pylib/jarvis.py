#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shadow
"""

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "dd"
        ) from exc
    print(sys.argv)
    # execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

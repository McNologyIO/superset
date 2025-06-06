FROM apache/superset:master

USER root

# Install uv globally (if not preinstalled)
RUN pip install uv

# Create venv manually if needed
RUN python -m venv /app/.venv

# Install deps with uv using the venv path
RUN /app/.venv/bin/uv pip install \
    psycopg2-binary \
    pymssql \
    Authlib \
    openpyxl \
    pillow \
    playwright \
    && playwright install-deps \
    && PLAYWRIGHT_BROWSERS_PATH=/usr/local/share/playwright-browsers playwright install chromium

USER superset

CMD ["/app/docker/entrypoints/run-server.sh"]

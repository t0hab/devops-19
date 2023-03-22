import sentry_sdk
sentry_sdk.init(
    dsn="https://24517ad50074447798e14a85ca637874@o4504881037508608.ingest.sentry.io/4504881074208768",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    environment="development",
    release="1.0"
)

if __name__ == "__main__":
    devision_zero = 1 /0
#!/bin/bash

set -e

# first check if we're passing flags, if so
# prepend with sentry
if [ "${1:0:1}" = '-' ]; then
	set -- sentry "$@"
fi
case "$1" in
	celery|cleanup|config|createuser|devserver|django|exec|export|help|import|init|plugins|queues|repair|run|shell|start|tsdb|upgrade)
		set -- sentry "$@"
		;;
	configure_options|generate_token)
		script_name="$1"
		shift
		export PYTHONPATH="/usr/local/scripts/sentry/"
		set -- sentry exec "/usr/local/scripts/sentry/${script_name}.py"
		;;
	generate_dsn)
		script_name="$1"
		shift
		auth_token="$1"
		shift
		export PYTHONPATH="/usr/local/scripts/sentry/"
		# We cannot pass the arguments via sentry exec so we pass them through env vars.
		export SENTRY_AUTH_TOKEN="${auth_token}"
		set -- sentry exec "/usr/local/scripts/sentry/${script_name}.py"
		;;
esac

if [ "$1" = 'sentry' ]; then
	set -- tini -- "$@"
	if [ "$(id -u)" = '0' ]; then
		mkdir -p "$SENTRY_FILESTORE_DIR"
		chown -R sentry "$SENTRY_FILESTORE_DIR"
		set -- gosu sentry "$@"
	fi
fi

exec "$@"

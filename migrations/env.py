# Import your Flask app factory and SQLAlchemy instance
import os
from app import create_app, db
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Load the application and bind to the database
config_name = os.environ.get('CONFIG_NAME') or 'default'
app = create_app(config_name)
app.app_context().push()

# Use the database URL from your Flask app
config = context.config
config.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])

# Set up logging
fileConfig(config.config_file_name)

# Add your model's MetaData object here
target_metadata = db.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

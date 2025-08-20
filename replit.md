# Overview

This is a Telegram bot built with Python using the python-telegram-bot library. The bot provides basic functionality including command handling (/start, /help), text message processing, and comprehensive error handling with logging capabilities. It's designed as a foundation for building more complex Telegram bot applications.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Bot Framework
The application uses the python-telegram-bot library as the core framework, leveraging its asynchronous capabilities for handling concurrent user interactions. The bot follows an event-driven architecture pattern where handlers respond to specific user actions (commands and messages).

## Application Structure
The codebase follows a modular design with clear separation of concerns:
- `bot.py` - Main application entry point and bot initialization
- `config.py` - Configuration management and environment variable handling
- `handlers.py` - Event handlers for commands and messages

## Configuration Management
Environment variables are managed through python-dotenv, allowing secure token storage and flexible configuration options. The bot token is mandatory and retrieved from environment variables, with proper validation to prevent startup without credentials.

## Logging Strategy
Comprehensive logging system with dual output streams - both file-based logging (bot.log) and console output. All user interactions and errors are tracked with appropriate log levels for debugging and monitoring.

## Error Handling
Centralized error handling mechanism with graceful degradation - errors are logged while providing user-friendly error messages to maintain bot availability.

## Message Processing
Asynchronous message handling using filters to distinguish between commands and regular text messages, enabling scalable concurrent user interactions.

# External Dependencies

## Core Dependencies
- `python-telegram-bot` - Primary framework for Telegram Bot API integration
- `python-dotenv` - Environment variable management for secure configuration

## Telegram Bot API
Direct integration with Telegram's Bot API for real-time message processing and user interaction management.

## Environment Variables
- `TELEGRAM_BOT_TOKEN` (required) - Bot authentication token from BotFather
- `DEBUG` (optional) - Debug mode toggle
- `LOG_LEVEL` (optional) - Logging verbosity control
- `BOT_NAME` (optional) - Bot display name customization
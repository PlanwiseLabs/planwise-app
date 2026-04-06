# Planwise – Frontend

Next.js 15 (TypeScript) application for the Planwise web interface.

## Stack

- **Next.js 15** – React framework with App Router
- **TypeScript** – static typing
- **React 19** – UI library

## Getting Started

### Prerequisites

- Node.js 20+
- npm / yarn / pnpm

### Setup

```bash
# Install dependencies
npm install

# Copy environment variables
cp .env.example .env.local
# Edit .env.local with your values

# Run the development server
npm run dev
```

The app will be available at `http://localhost:3000`.

## Project Structure

```
frontend/
├── next.config.ts        # Next.js configuration
├── tsconfig.json         # TypeScript configuration
├── package.json
└── src/
    ├── app/
    │   ├── layout.tsx    # Root layout
    │   ├── page.tsx      # Home page
    │   └── globals.css   # Global styles
    ├── components/       # Reusable UI components
    └── lib/
        └── api.ts        # API client helpers
```

## Available Scripts

| Command              | Description                       |
|----------------------|-----------------------------------|
| `npm run dev`        | Start development server          |
| `npm run build`      | Build for production              |
| `npm run start`      | Start production server           |
| `npm run lint`       | Run ESLint                        |
| `npm run type-check` | Run TypeScript type checker       |

# Frontend

Recommended frontend:

- Next.js
- Tailwind
- shadcn/ui
- React Flow
- Recharts

Create the actual app with:

npx create-next-app@latest frontend --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
cd frontend
npm install reactflow recharts lucide-react
npx shadcn@latest init

Main dashboard panels:

- Incident Overview
- Band Collaboration Feed
- Agent Status
- Evidence Board
- Timeline
- Final Incident Report

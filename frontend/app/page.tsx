import InfoCard from "../components/InfoCard";

const mockData = {
  today: [
    { title: "AI model update", summary: "New transformer variant improves efficiency.", source: "Tech RSS" },
    { title: "Macro outlook", summary: "Summary of this week's macro indicators.", source: "Newsletter" },
  ],
  week: [
    { title: "Product launch", summary: "Upcoming launch timeline and key milestones.", source: "Internal" },
    { title: "Earnings preview", summary: "Analysts expect moderate growth for Q3.", source: "Markets" },
  ],
  background: [
    { title: "Reading list", summary: "Long-form essays queued for later.", source: "Bookmarks" },
    { title: "Trade signals", summary: "Parsed signals ready for validation.", source: "Telegram" },
  ],
};

const columns = [
  { title: "Today", key: "today" as const },
  { title: "This Week", key: "week" as const },
  { title: "Background", key: "background" as const },
];

export default function DashboardPage() {
  return (
    <main className="mx-auto max-w-6xl space-y-8 px-6 py-10">
      <header>
        <h1 className="text-3xl font-bold text-white">InfoHarbor Dashboard</h1>
        <p className="mt-2 text-gray-400">Curated information cards to focus your attention.</p>
      </header>
      <div className="grid gap-6 md:grid-cols-3">
        {columns.map((column) => (
          <section key={column.key} className="space-y-4">
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold text-white">{column.title}</h2>
              <span className="text-sm text-gray-500">{mockData[column.key].length} items</span>
            </div>
            <div className="space-y-3">
              {mockData[column.key].map((card) => (
                <InfoCard key={card.title} {...card} />
              ))}
            </div>
          </section>
        ))}
      </div>
    </main>
  );
}

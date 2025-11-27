interface InfoCardProps {
  title: string;
  summary: string;
  source: string;
}

export function InfoCard({ title, summary, source }: InfoCardProps) {
  return (
    <div className="rounded-lg border border-gray-800 bg-gray-900 p-4 shadow-sm">
      <div className="text-sm text-gray-400">{source}</div>
      <h3 className="mt-1 text-lg font-semibold text-white">{title}</h3>
      <p className="mt-2 text-sm text-gray-300 leading-relaxed">{summary}</p>
    </div>
  );
}
export default InfoCard;

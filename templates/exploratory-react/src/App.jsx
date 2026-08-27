import React, { useMemo, useState } from 'react';

const signals = [
  {
    id: 'clarity',
    category: 'Insight',
    label: 'Clarity before volume',
    value: 82,
    note: 'A smaller set of explicit claims is easier to test and remember.',
    implication: 'Remove material that does not change the audience’s understanding.',
  },
  {
    id: 'sequence',
    category: 'Process',
    label: 'Sequence earns trust',
    value: 67,
    note: 'Evidence is strongest when it appears beside the claim it supports.',
    implication: 'Keep the route from thesis to proof visible.',
  },
  {
    id: 'choice',
    category: 'Decision',
    label: 'Choice needs criteria',
    value: 74,
    note: 'Alternatives become useful only when the audience knows how they are evaluated.',
    implication: 'State decision criteria before comparing options.',
  },
  {
    id: 'inspection',
    category: 'Process',
    label: 'Rendering reveals reality',
    value: 91,
    note: 'A successful build cannot expose visual hierarchy, crop, density, or rhythm defects.',
    implication: 'Inspect, correct, and re-render before review.',
  },
];

const categories = ['All', ...new Set(signals.map((signal) => signal.category))];

export default function App() {
  const [filter, setFilter] = useState('All');
  const [selectedId, setSelectedId] = useState(null);

  const visibleSignals = useMemo(
    () => signals.filter((signal) => filter === 'All' || signal.category === filter),
    [filter],
  );

  const selected = signals.find((signal) => signal.id === selectedId) ?? null;

  function chooseFilter(category) {
    setFilter(category);
    if (selected && category !== 'All' && selected.category !== category) {
      setSelectedId(null);
    }
  }

  function reset() {
    setFilter('All');
    setSelectedId(null);
  }

  return (
    <main className="experience-shell">
      <header className="masthead">
        <div>
          <p className="kicker">Replaceable exploratory example</p>
          <h1>Signal Atlas</h1>
        </div>
        <p className="intro">
          A local-data shell for filters, selection, detail, and reset. The final experience must be shaped by an approved narrative.
        </p>
      </header>

      <section className="explorer" aria-label="Explore example signals">
        <aside className="filters" aria-label="Filter signals by category">
          <p className="section-label">Filter</p>
          <div className="filter-list">
            {categories.map((category) => (
              <button
                key={category}
                type="button"
                aria-pressed={filter === category}
                onClick={() => chooseFilter(category)}
              >
                <span>{category}</span>
                <span>{category === 'All' ? signals.length : signals.filter((signal) => signal.category === category).length}</span>
              </button>
            ))}
          </div>
          <button className="reset" type="button" onClick={reset} disabled={filter === 'All' && !selected}>
            Reset view
          </button>
        </aside>

        <div className="signal-list" aria-live="polite">
          <div className="list-heading">
            <p className="section-label">{filter} signals</p>
            <span>{visibleSignals.length} visible</span>
          </div>
          {visibleSignals.map((signal, index) => (
            <button
              className="signal-row"
              key={signal.id}
              type="button"
              aria-pressed={selectedId === signal.id}
              onClick={() => setSelectedId(signal.id)}
            >
              <span className="row-index">{String(index + 1).padStart(2, '0')}</span>
              <span className="row-copy">
                <small>{signal.category}</small>
                <strong>{signal.label}</strong>
              </span>
              <span className="row-value" aria-label={`Example score ${signal.value} out of 100`}>{signal.value}</span>
              <span className="row-mark" aria-hidden="true">↗</span>
            </button>
          ))}
        </div>

        <aside className="detail" aria-live="polite" aria-label="Selected signal detail">
          {selected ? (
            <div className="detail-content">
              <p className="section-label">Selected · {selected.category}</p>
              <div className="detail-score" aria-hidden="true">{selected.value}</div>
              <h2>{selected.label}</h2>
              <p>{selected.note}</p>
              <div className="implication">
                <span>Implication</span>
                <strong>{selected.implication}</strong>
              </div>
            </div>
          ) : (
            <div className="empty-detail">
              <span aria-hidden="true">↗</span>
              <p>Select a signal to reveal its evidence and implication.</p>
            </div>
          )}
        </aside>
      </section>
    </main>
  );
}

/* ==========================================================================
   MIRA Health Records — Design Tokens
   --------------------------------------------------------------------------
   Palette:
     --navy        #0B2545  deep clinical navy — headers, primary text accents
     --ink         #1A1F26  body text
     --slate-bg    #F4F6F8  page background
     --teal        #0FA3A3  vital-sign accent — primary actions, "low risk"
     --coral       #E0563D  alert accent — "high risk", destructive actions
     --amber       #D98C2E  "moderate risk"
     --white       #FFFFFF  cards
   Type:
     Space Grotesk — display / headings (technical, monitor-like character)
     Inter         — body copy and UI labels
     JetBrains Mono — lab values and dates (numeric precision)
   ========================================================================== */

:root {
    --navy: #0B2545;
    --navy-soft: #15356B;
    --ink: #1A1F26;
    --ink-muted: #5B6573;
    --slate-bg: #F4F6F8;
    --slate-line: #E2E7EC;
    --teal: #0FA3A3;
    --teal-dark: #0B7F7F;
    --coral: #E0563D;
    --coral-soft: #FBE8E4;
    --amber: #D98C2E;
    --amber-soft: #FBF0E0;
    --teal-soft: #E2F5F4;
    --white: #FFFFFF;

    --radius-card: 14px;
    --radius-control: 10px;
    --shadow-card: 0 1px 2px rgba(11, 37, 69, 0.04), 0 8px 24px rgba(11, 37, 69, 0.06);
    --shadow-card-hover: 0 4px 8px rgba(11, 37, 69, 0.06), 0 16px 32px rgba(11, 37, 69, 0.09);
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}

* { box-sizing: border-box; }

html, body {
    margin: 0;
    background: var(--slate-bg);
    color: var(--ink);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 15px;
    line-height: 1.55;
}

h1, h2, h3, .brand-name {
    font-family: 'Space Grotesk', 'Inter', sans-serif;
    color: var(--navy);
    font-weight: 600;
    letter-spacing: -0.01em;
    margin: 0;
}

a { color: var(--teal-dark); text-decoration: none; }
a:hover { text-decoration: underline; }

.container-app {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 24px;
}

/* ---------------------------------------------------------------------- */
/* Header                                                                  */
/* ---------------------------------------------------------------------- */

.app-header {
    background: var(--navy);
    border-bottom: 3px solid var(--teal);
}

.app-header .container-app {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 76px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    color: var(--white);
}
.brand:hover { text-decoration: none; }

.brand-mark {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background: var(--teal);
    color: var(--navy);
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.brand-text { display: flex; flex-direction: column; line-height: 1.2; }
.brand-name { color: var(--white); font-size: 1.15rem; }
.brand-sub { font-size: 0.72rem; color: #9FB3CC; letter-spacing: 0.02em; }

.header-nav { display: flex; align-items: center; gap: 18px; }

.nav-link {
    color: #C7D4E6;
    font-weight: 500;
    font-size: 0.92rem;
    display: flex;
    align-items: center;
    gap: 6px;
}
.nav-link:hover { color: var(--white); text-decoration: none; }
.nav-link.active { color: var(--teal); }

/* ---------------------------------------------------------------------- */
/* Buttons                                                                 */
/* ---------------------------------------------------------------------- */

.btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.88rem;
    padding: 10px 18px;
    border-radius: var(--radius-control);
    border: 1px solid transparent;
    cursor: pointer;
    transition: background-color 0.15s ease, border-color 0.15s ease, transform 0.1s ease;
}
.btn:hover { text-decoration: none; }
.btn:active { transform: translateY(1px); }
.btn:focus-visible {
    outline: 2px solid var(--teal);
    outline-offset: 2px;
}

.btn-accent {
    background: var(--teal);
    color: var(--navy);
}
.btn-accent:hover { background: #14B8B8; color: var(--navy); }

.btn-ghost {
    background: transparent;
    color: var(--navy);
    border-color: var(--slate-line);
}
.btn-ghost:hover { background: var(--white); border-color: var(--navy); }

.btn-danger {
    background: var(--coral);
    color: var(--white);
}
.btn-danger:hover { background: #C8442C; }

/* ---------------------------------------------------------------------- */
/* Main layout / page intro                                               */
/* ---------------------------------------------------------------------- */

.app-main { padding: 40px 24px 64px; min-height: calc(100vh - 76px - 90px); }

.page-intro { max-width: 640px; margin-bottom: 28px; }

.eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--teal-dark);
    margin: 0 0 6px;
}

.page-intro h1 { font-size: 1.9rem; margin-bottom: 8px; }
.page-lede { color: var(--ink-muted); margin: 0; font-size: 0.96rem; }

/* ---------------------------------------------------------------------- */
/* Toolbar / search                                                        */
/* ---------------------------------------------------------------------- */

.toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.search-form {
    position: relative;
    flex: 1;
    min-width: 240px;
    max-width: 420px;
    display: flex;
    align-items: center;
}
.search-form i.bi-search {
    position: absolute;
    left: 14px;
    color: var(--ink-muted);
    font-size: 0.9rem;
}
.search-form input {
    width: 100%;
    padding: 10px 36px 10px 38px;
    border: 1px solid var(--slate-line);
    border-radius: var(--radius-control);
    background: var(--white);
    font-size: 0.9rem;
    color: var(--ink);
}
.search-form input:focus {
    outline: none;
    border-color: var(--teal);
    box-shadow: 0 0 0 3px var(--teal-soft);
}
.clear-search {
    position: absolute;
    right: 12px;
    color: var(--ink-muted);
}

.record-count {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: var(--ink-muted);
    white-space: nowrap;
}

/* ---------------------------------------------------------------------- */
/* Records table                                                           */
/* ---------------------------------------------------------------------- */

.table-card {
    background: var(--white);
    border-radius: var(--radius-card);
    box-shadow: var(--shadow-card);
    overflow: hidden;
    overflow-x: auto;
}

.records-table { width: 100%; border-collapse: collapse; min-width: 760px; }

.records-table thead th {
    text-align: left;
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--ink-muted);
    padding: 14px 16px;
    border-bottom: 1px solid var(--slate-line);
    background: #FAFBFC;
    white-space: nowrap;
}

.records-table td {
    padding: 14px 16px;
    border-bottom: 1px solid var(--slate-line);
    vertical-align: middle;
    font-size: 0.9rem;
}
.records-table tbody tr:last-child td { border-bottom: none; }
.records-table tbody tr:hover { background: #FAFBFC; }

.text-end { text-align: right; }

.mono-cell {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: var(--ink);
}

.patient-cell { display: flex; flex-direction: column; }
.patient-name { font-weight: 600; color: var(--navy); }
.patient-email { font-size: 0.78rem; color: var(--ink-muted); }

.row-actions { display: flex; gap: 6px; justify-content: flex-end; }

.icon-btn {
    width: 32px;
    height: 32px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    color: var(--ink-muted);
    border: 1px solid transparent;
    background: transparent;
    cursor: pointer;
    font-size: 0.95rem;
}
.icon-btn:hover { background: var(--slate-bg); color: var(--navy); }
.icon-btn-danger:hover { background: var(--coral-soft); color: var(--coral); }

/* ---------------------------------------------------------------------- */
/* Risk pills                                                              */
/* ---------------------------------------------------------------------- */

.risk-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 999px;
    white-space: nowrap;
}
.risk-pill i { font-size: 0.5rem; }

.risk-low { background: var(--teal-soft); color: var(--teal-dark); }
.risk-moderate { background: var(--amber-soft); color: #9A6213; }
.risk-high { background: var(--coral-soft); color: var(--coral); }

/* ---------------------------------------------------------------------- */
/* Empty / error state                                                     */
/* ---------------------------------------------------------------------- */

.empty-state {
    background: var(--white);
    border-radius: var(--radius-card);
    box-shadow: var(--shadow-card);
    padding: 64px 32px;
    text-align: center;
    color: var(--ink-muted);
}
.empty-state i { font-size: 2.4rem; color: var(--teal); margin-bottom: 14px; display: block; }
.empty-state h2 { font-size: 1.2rem; margin-bottom: 8px; }
.empty-state p { margin-bottom: 18px; }
.error-state i { color: var(--coral); }

/* ---------------------------------------------------------------------- */
/* Forms                                                                   */
/* ---------------------------------------------------------------------- */

.form-card {
    background: var(--white);
    border-radius: var(--radius-card);
    box-shadow: var(--shadow-card);
    padding: 32px;
    max-width: 760px;
}

.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.form-field-wide { grid-column: 1 / -1; }

.form-section-label {
    grid-column: 1 / -1;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--teal-dark);
    border-top: 1px solid var(--slate-line);
    padding-top: 18px;
    margin-top: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.form-field { display: flex; flex-direction: column; gap: 6px; }

.form-field label {
    font-size: 0.83rem;
    font-weight: 600;
    color: var(--navy);
}

.unit-tag {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    font-size: 0.72rem;
    color: var(--ink-muted);
    text-transform: lowercase;
    margin-left: 4px;
}

.form-field input {
    padding: 10px 12px;
    border: 1px solid var(--slate-line);
    border-radius: var(--radius-control);
    font-size: 0.92rem;
    font-family: 'Inter', sans-serif;
    color: var(--ink);
    background: var(--white);
}
.mono-input { font-family: 'JetBrains Mono', monospace !important; }

.form-field input:focus {
    outline: none;
    border-color: var(--teal);
    box-shadow: 0 0 0 3px var(--teal-soft);
}
.form-field input.is-invalid {
    border-color: var(--coral);
    box-shadow: 0 0 0 3px var(--coral-soft);
}

.field-error {
    color: var(--coral);
    font-size: 0.78rem;
    margin: 0;
}

.remark-preview {
    padding: 12px 14px;
    border-radius: var(--radius-control);
    font-size: 0.88rem;
    display: flex;
    gap: 8px;
    align-items: flex-start;
}
.remark-preview.risk-low { background: var(--teal-soft); color: var(--teal-dark); }
.remark-preview.risk-moderate { background: var(--amber-soft); color: #9A6213; }
.remark-preview.risk-high { background: var(--coral-soft); color: var(--coral); }

.form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 28px;
    padding-top: 20px;
    border-top: 1px solid var(--slate-line);
}

/* ---------------------------------------------------------------------- */
/* Detail page                                                             */
/* ---------------------------------------------------------------------- */

.back-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--ink-muted);
    margin-bottom: 20px;
}
.back-link:hover { color: var(--navy); text-decoration: none; }

.detail-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 24px;
    flex-wrap: wrap;
}
.detail-header h1 { font-size: 1.7rem; margin: 4px 0; }

.vitals-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: var(--slate-line);
    border-radius: var(--radius-card);
    overflow: hidden;
    box-shadow: var(--shadow-card);
    margin-bottom: 20px;
}
.vital {
    background: var(--navy);
    padding: 22px 24px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.vital-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #9FB3CC;
}
.vital-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.7rem;
    font-weight: 600;
    color: var(--white);
}
.vital-unit {
    font-size: 0.8rem;
    color: #9FB3CC;
    margin-left: 6px;
    font-weight: 500;
}

.remark-card {
    background: var(--white);
    border-radius: var(--radius-card);
    box-shadow: var(--shadow-card);
    padding: 22px 24px;
    border-left: 4px solid var(--teal);
    margin-bottom: 16px;
}
.remark-card.risk-moderate { border-left-color: var(--amber); }
.remark-card.risk-high { border-left-color: var(--coral); }

.remark-card-header {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 10px;
    font-size: 0.9rem;
}
.remark-card-header .risk-pill { margin-left: auto; }
.remark-text { margin: 0; color: var(--ink); line-height: 1.6; }

.record-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--ink-muted);
}

/* ---------------------------------------------------------------------- */
/* Flash toasts                                                            */
/* ---------------------------------------------------------------------- */

.flash-stack { display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px; }

.flash-toast {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 13px 16px;
    border-radius: var(--radius-control);
    font-size: 0.88rem;
    font-weight: 500;
}
.flash-success { background: var(--teal-soft); color: var(--teal-dark); }
.flash-danger { background: var(--coral-soft); color: var(--coral); }
.flash-warning { background: var(--amber-soft); color: #9A6213; }

/* ---------------------------------------------------------------------- */
/* Footer                                                                  */
/* ---------------------------------------------------------------------- */

.app-footer {
    background: var(--white);
    border-top: 1px solid var(--slate-line);
    padding: 20px 24px;
    text-align: center;
}
.app-footer p {
    margin: 2px 0;
    font-size: 0.8rem;
    color: var(--ink-muted);
}
.footer-disclaimer { font-size: 0.74rem; }

/* ---------------------------------------------------------------------- */
/* Modal (Bootstrap overrides to match design system)                     */
/* ---------------------------------------------------------------------- */

.modal-content { border-radius: var(--radius-card); border: none; }
.modal-header, .modal-footer { border-color: var(--slate-line); }
.modal-title { font-family: 'Space Grotesk', sans-serif; color: var(--navy); }

/* ---------------------------------------------------------------------- */
/* Responsive                                                              */
/* ---------------------------------------------------------------------- */

@media (max-width: 720px) {
    .app-header .container-app { height: auto; padding: 14px 20px; flex-wrap: wrap; gap: 12px; }
    .brand-sub { display: none; }
    .form-grid { grid-template-columns: 1fr; }
    .vitals-strip { grid-template-columns: 1fr; }
    .detail-header { flex-direction: column; }
    .app-main { padding: 28px 16px 48px; }
}

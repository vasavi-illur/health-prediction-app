{% extends "base.html" %}
{% block title %}{{ "Edit record" if mode == "edit" else "New record" }} — MIRA{% endblock %}

{% block content %}

<section class="page-intro">
    <p class="eyebrow">{{ "Editing existing record" if mode == "edit" else "New patient" }}</p>
    <h1>{{ "Edit health record" if mode == "edit" else "Add a health record" }}</h1>
    <p class="page-lede">Enter the patient's details and latest lab values. The AI risk remark is generated automatically when you save.</p>
</section>

<div class="form-card">
    <form method="post" novalidate>
        <div class="form-grid">

            <div class="form-field form-field-wide">
                <label for="full_name">Full name</label>
                <input
                    type="text"
                    id="full_name"
                    name="full_name"
                    value="{{ form_data['full_name'] if form_data else '' }}"
                    class="{{ 'is-invalid' if errors.get('full_name') }}"
                    placeholder="e.g. Maria Gonzalez"
                    required
                >
                {% if errors.get('full_name') %}<p class="field-error">{{ errors['full_name'] }}</p>{% endif %}
            </div>

            <div class="form-field">
                <label for="date_of_birth">Date of birth</label>
                <input
                    type="date"
                    id="date_of_birth"
                    name="date_of_birth"
                    value="{{ form_data['date_of_birth'] if form_data else '' }}"
                    class="{{ 'is-invalid' if errors.get('date_of_birth') }}"
                    max="{{ today }}"
                    required
                >
                {% if errors.get('date_of_birth') %}<p class="field-error">{{ errors['date_of_birth'] }}</p>{% endif %}
            </div>

            <div class="form-field">
                <label for="email">Email address</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    value="{{ form_data['email'] if form_data else '' }}"
                    class="{{ 'is-invalid' if errors.get('email') }}"
                    placeholder="patient@example.com"
                    required
                >
                {% if errors.get('email') %}<p class="field-error">{{ errors['email'] }}</p>{% endif %}
            </div>

            <div class="form-section-label">
                <i class="bi bi-droplet-half"></i> Lab values
            </div>

            <div class="form-field">
                <label for="glucose">Glucose <span class="unit-tag">mg/dL</span></label>
                <input
                    type="number" step="0.1" inputmode="decimal"
                    id="glucose"
                    name="glucose"
                    value="{{ form_data['glucose'] if form_data else '' }}"
                    class="mono-input {{ 'is-invalid' if errors.get('glucose') }}"
                    placeholder="e.g. 95"
                    required
                >
                {% if errors.get('glucose') %}<p class="field-error">{{ errors['glucose'] }}</p>{% endif %}
            </div>

            <div class="form-field">
                <label for="haemoglobin">Haemoglobin <span class="unit-tag">g/dL</span></label>
                <input
                    type="number" step="0.1" inputmode="decimal"
                    id="haemoglobin"
                    name="haemoglobin"
                    value="{{ form_data['haemoglobin'] if form_data else '' }}"
                    class="mono-input {{ 'is-invalid' if errors.get('haemoglobin') }}"
                    placeholder="e.g. 14.2"
                    required
                >
                {% if errors.get('haemoglobin') %}<p class="field-error">{{ errors['haemoglobin'] }}</p>{% endif %}
            </div>

            <div class="form-field">
                <label for="cholesterol">Cholesterol <span class="unit-tag">mg/dL</span></label>
                <input
                    type="number" step="0.1" inputmode="decimal"
                    id="cholesterol"
                    name="cholesterol"
                    value="{{ form_data['cholesterol'] if form_data else '' }}"
                    class="mono-input {{ 'is-invalid' if errors.get('cholesterol') }}"
                    placeholder="e.g. 180"
                    required
                >
                {% if errors.get('cholesterol') %}<p class="field-error">{{ errors['cholesterol'] }}</p>{% endif %}
            </div>

            {% if mode == "edit" and patient and patient['remarks'] %}
            <div class="form-field form-field-wide">
                <label>Current AI remark <span class="unit-tag">recalculated on save</span></label>
                <div class="remark-preview risk-{{ patient['risk_level'] }}">
                    <i class="bi bi-robot"></i> {{ patient['remarks'] }}
                </div>
            </div>
            {% endif %}

        </div>

        <div class="form-actions">
            <a href="{{ url_for('main.index') }}" class="btn btn-ghost">Cancel</a>
            <button type="submit" class="btn btn-accent">
                <i class="bi bi-check-lg"></i>
                {{ "Save changes" if mode == "edit" else "Create record" }}
            </button>
        </div>
    </form>
</div>

{% endblock %}

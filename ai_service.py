{% extends "base.html" %}
{% block title %}Patient Records — MIRA{% endblock %}

{% block content %}

<section class="page-intro">
    <p class="eyebrow">Patient registry</p>
    <h1>Health records</h1>
    <p class="page-lede">Every record below was scored the moment it was saved &mdash; glucose, haemoglobin, and cholesterol checked against reference ranges to flag risk in the Remarks column.</p>
</section>

<section class="toolbar">
    <form class="search-form" method="get" action="{{ url_for('main.index') }}">
        <i class="bi bi-search"></i>
        <input
            type="search"
            name="q"
            value="{{ search_query }}"
            placeholder="Search by name or email&hellip;"
            aria-label="Search patient records"
        >
        {% if search_query %}
            <a href="{{ url_for('main.index') }}" class="clear-search" aria-label="Clear search">
                <i class="bi bi-x-circle-fill"></i>
            </a>
        {% endif %}
    </form>
    <span class="record-count">{{ patients|length }} record{{ 's' if patients|length != 1 else '' }}</span>
</section>

{% if patients %}
<div class="table-card">
    <table class="records-table">
        <thead>
            <tr>
                <th scope="col">Patient</th>
                <th scope="col">Date of birth</th>
                <th scope="col" class="text-end">Glucose</th>
                <th scope="col" class="text-end">Haemoglobin</th>
                <th scope="col" class="text-end">Cholesterol</th>
                <th scope="col">AI remarks</th>
                <th scope="col" class="text-end">Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for patient in patients %}
            <tr>
                <td>
                    <div class="patient-cell">
                        <span class="patient-name">{{ patient['full_name'] }}</span>
                        <span class="patient-email">{{ patient['email'] }}</span>
                    </div>
                </td>
                <td class="mono-cell">{{ patient['date_of_birth'] }}</td>
                <td class="text-end mono-cell">{{ "%.1f"|format(patient['glucose']) }}</td>
                <td class="text-end mono-cell">{{ "%.1f"|format(patient['haemoglobin']) }}</td>
                <td class="text-end mono-cell">{{ "%.1f"|format(patient['cholesterol']) }}</td>
                <td>
                    <span class="risk-pill risk-{{ patient['risk_level'] }}">
                        <i class="bi bi-circle-fill"></i>
                        {{ patient['risk_level']|capitalize }}
                    </span>
                </td>
                <td class="text-end">
                    <div class="row-actions">
                        <a href="{{ url_for('main.view_patient', patient_id=patient['id']) }}" class="icon-btn" title="View" aria-label="View {{ patient['full_name'] }}">
                            <i class="bi bi-eye"></i>
                        </a>
                        <a href="{{ url_for('main.edit_patient', patient_id=patient['id']) }}" class="icon-btn" title="Edit" aria-label="Edit {{ patient['full_name'] }}">
                            <i class="bi bi-pencil"></i>
                        </a>
                        <button
                            type="button"
                            class="icon-btn icon-btn-danger"
                            title="Delete"
                            aria-label="Delete {{ patient['full_name'] }}"
                            data-bs-toggle="modal"
                            data-bs-target="#deleteModal"
                            data-patient-id="{{ patient['id'] }}"
                            data-patient-name="{{ patient['full_name'] }}"
                        >
                            <i class="bi bi-trash3"></i>
                        </button>
                    </div>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% else %}
<div class="empty-state">
    <i class="bi bi-clipboard2-pulse"></i>
    {% if search_query %}
        <h2>No matches for &ldquo;{{ search_query }}&rdquo;</h2>
        <p>Try a different name or email, or <a href="{{ url_for('main.index') }}">clear the search</a>.</p>
    {% else %}
        <h2>No patient records yet</h2>
        <p>Add your first record to see an AI-generated risk remark appear automatically.</p>
        <a href="{{ url_for('main.create_patient') }}" class="btn btn-accent">
            <i class="bi bi-plus-lg"></i> New record
        </a>
    {% endif %}
</div>
{% endif %}

<!-- Delete confirmation modal: one shared modal, populated via JS from data-* attributes -->
<div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="deleteModalLabel">Delete record</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>Are you sure you want to delete the record for <strong id="deletePatientName"></strong>? This cannot be undone.</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-ghost" data-bs-dismiss="modal">Cancel</button>
                <form id="deleteForm" method="post" action="">
                    <button type="submit" class="btn btn-danger">Delete record</button>
                </form>
            </div>
        </div>
    </div>
</div>

{% endblock %}

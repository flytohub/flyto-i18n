#!/usr/bin/env python3
"""Fill all empty English values in cloud locale files."""
import json
import re
from pathlib import Path

CLOUD_EN = Path(__file__).parent.parent / 'locales' / 'cloud' / 'en'

def key_to_english(key):
    """Generate English text from a key name."""
    parts = key.split('.')
    # Use last 1-2 segments for the label
    if len(parts) >= 2:
        last = parts[-1]
        parent = parts[-2] if len(parts) >= 3 else ''
    else:
        last = parts[-1]
        parent = ''

    # camelCase to words
    words = re.sub(r'([a-z])([A-Z])', r'\1 \2', last)
    words = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', words)
    result = words[0].upper() + words[1:] if words else last

    return result

# Contextual translations for known patterns
MANUAL = {
    # admin.landingPage.*
    "admin.landingPage.actions": "Actions",
    "admin.landingPage.company": "Company",
    "admin.landingPage.confirmDelete": "Confirm Delete",
    "admin.landingPage.confirmDeleteMessage": "Are you sure you want to delete this item? This action cannot be undone.",
    "admin.landingPage.contact": "Contact",
    "admin.landingPage.contactDetails": "Contact Details",
    "admin.landingPage.contactSubmissions": "Contact Submissions",
    "admin.landingPage.delete": "Delete",
    "admin.landingPage.deleted": "Deleted successfully",
    "admin.landingPage.desktopApp": "Desktop App",
    "admin.landingPage.desktopSubscribers": "Desktop Subscribers",
    "admin.landingPage.email": "Email",
    "admin.landingPage.exportCsv": "Export CSV",
    "admin.landingPage.exported": "Exported successfully",
    "admin.landingPage.items": "items",
    "admin.landingPage.license": "License",
    "admin.landingPage.licenseDetails": "License Details",
    "admin.landingPage.licenseRequests": "License Requests",
    "admin.landingPage.message": "Message",
    "admin.landingPage.name": "Name",
    "admin.landingPage.noData": "No data available",
    "admin.landingPage.nodeSubscribers": "Node.js Subscribers",
    "admin.landingPage.nodejs": "Node.js",
    "admin.landingPage.notified": "Notified",
    "admin.landingPage.release": "Release",
    "admin.landingPage.releaseSubscribers": "Release Subscribers",
    "admin.landingPage.reply": "Reply",
    "admin.landingPage.source": "Source",
    "admin.landingPage.subject": "Subject",
    "admin.landingPage.submittedAt": "Submitted at",
    "admin.landingPage.subscribedAt": "Subscribed at",
    "admin.landingPage.subtitle": "Manage landing page data and subscribers",
    "admin.landingPage.useCase": "Use Case",
    "admin.landingPage.view": "View",
    "admin.landingPage.wasmSubscribers": "WebAssembly Subscribers",
    "admin.landingPage.webAssembly": "WebAssembly",
    "admin.nav.landingPage": "Landing Page",

    # common
    "common.noResults": "No results found",

    # debug
    "debug.toolbar.evolution": "Evolution",

    # executionHistory
    "executionHistory.stopFailed": "Failed to stop execution",
    "executionHistory.stopped": "Execution stopped",

    # http
    "http.authType.credential": "Credential",

    # plugins
    "plugins.load": "Load Plugin",
    "plugins.noDescription": "No description available",

    # rpa
    "rpa.actions.disconnect": "Disconnect",
    "rpa.actions.record": "Record",
    "rpa.agents.connect": "Connect Agent",
    "rpa.agents.connectFirst": "Connect an agent to get started",
    "rpa.agents.empty": "No agents connected",
    "rpa.agents.title": "RPA Agents",
    "rpa.connect.codeExpires": "Code expires in",
    "rpa.connect.step1": "Download and install the Flyto RPA agent",
    "rpa.connect.step2": "Launch the agent and enter the connection code",
    "rpa.connect.step3": "Start automating browser tasks",
    "rpa.connect.title": "Connect RPA Agent",
    "rpa.connect.waiting": "Waiting for agent connection...",
    "rpa.elements.empty": "No elements captured yet",
    "rpa.elements.title": "Captured Elements",
    "rpa.log.title": "Activity Log",
    "rpa.quickActions.title": "Quick Actions",
    "rpa.recordings.empty": "No recordings yet",
    "rpa.recordings.run": "Run Recording",
    "rpa.recordings.title": "Recordings",
    "rpa.stats.agents": "Connected Agents",
    "rpa.stats.executions": "Total Executions",
    "rpa.stats.recordings": "Recordings",
    "rpa.stats.success": "Success Rate",

    # scheduler
    "scheduler.create.cron": "Cron Expression",
    "scheduler.create.event": "Event",
    "scheduler.create.interval": "Interval",
    "scheduler.create.name": "Schedule Name",
    "scheduler.create.namePlaceholder": "Enter schedule name...",
    "scheduler.create.priority": "Priority",
    "scheduler.create.runAt": "Run at",
    "scheduler.create.selectEvent": "Select event...",
    "scheduler.create.selectWorkflow": "Select workflow...",
    "scheduler.create.submit": "Create Schedule",
    "scheduler.create.title": "Create Schedule",
    "scheduler.create.type": "Schedule Type",
    "scheduler.create.unit": "Unit",
    "scheduler.create.workflow": "Workflow",
    "scheduler.disable": "Disable",
    "scheduler.enable": "Enable",
    "scheduler.nextRun": "Next Run",
    "scheduler.priority.high": "High",
    "scheduler.priority.low": "Low",
    "scheduler.schedules.create": "Create Schedule",
    "scheduler.schedules.empty": "No schedules yet",
    "scheduler.schedules.emptyDesc": "Create a schedule to automate workflow executions on a timer or event trigger.",
    "scheduler.schedules.title": "Schedules",
    "scheduler.stats.active": "Active Schedules",
    "scheduler.stats.completedToday": "Completed Today",
    "scheduler.stats.failedToday": "Failed Today",
    "scheduler.stats.runningJobs": "Running Jobs",
    "scheduler.status.disabled": "Disabled",
    "scheduler.triggerNow": "Trigger Now",
    "scheduler.upcoming.empty": "No upcoming runs",
    "scheduler.upcoming.title": "Upcoming Runs",

    # seo
    "seo.rankings.add": "Add Keyword",
    "seo.rankings.checkAll": "Check All Rankings",
    "seo.rankings.checkRanking": "Check Ranking",
    "seo.rankings.confirmRemove": "Are you sure you want to remove this keyword?",
    "seo.rankings.currentPosition": "Current Position",
    "seo.rankings.getApiKey": "Get API Key",
    "seo.rankings.keywordPlaceholder": "Enter keyword to track...",
    "seo.rankings.languageEn": "English",
    "seo.rankings.languageJa": "Japanese",
    "seo.rankings.languageZhTW": "Traditional Chinese",
    "seo.rankings.locationHK": "Hong Kong",
    "seo.rankings.locationJapan": "Japan",
    "seo.rankings.locationTaiwan": "Taiwan",
    "seo.rankings.locationUS": "United States",
    "seo.rankings.never": "Never",
    "seo.rankings.noKeywords": "No keywords tracked",
    "seo.rankings.noKeywordsDesc": "Add keywords to start tracking your search engine rankings.",
    "seo.rankings.notConfigured": "SEO Tracking Not Configured",
    "seo.rankings.notConfiguredDesc": "Set up your SerpAPI key to start tracking keyword rankings.",
    "seo.rankings.notInTop100": "Not in top 100",
    "seo.rankings.ourRankingResult": "Our Ranking Result",
    "seo.rankings.positionOnGoogle": "Position on Google",
    "seo.rankings.removeKeyword": "Remove Keyword",
    "seo.rankings.tableActions": "Actions",
    "seo.rankings.tableKeyword": "Keyword",
    "seo.rankings.tableLastChecked": "Last Checked",
    "seo.rankings.tableLocation": "Location",
    "seo.rankings.tablePosition": "Position",
    "seo.rankings.top10Results": "Top 10 Results",
    "seo.rankings.trackNewKeyword": "Track New Keyword",
    "seo.rankings.trackedKeywords": "Tracked Keywords",
    "seo.rankings.viewDetails": "View Details",

    # templateBuilder
    "templateBuilder.header.tidyNodes": "Tidy Nodes",
    "templateBuilder.messages.workflowLocked": "This workflow is locked and cannot be edited.",
    "templateBuilder.protectedWorkflow.description": "This workflow is protected. Changes are restricted to maintain stability.",
    "templateBuilder.protectedWorkflow.title": "Protected Workflow",
    "templateBuilder.tabs.protectedWorkflow": "Protection",

    # usage
    "usage.chart.noData": "No usage data available for this period",
    "usage.dashboard.currentUsage": "Current Usage",
    "usage.dashboard.title": "Usage Dashboard",
    "usage.dashboard.topModules": "Top Modules",
    "usage.dashboard.usageHistory": "Usage History",
    "usage.warning.execPaused": "Workflow executions have been paused due to plan limits.",
    "usage.warning.nearLimitMessage": "You are approaching your plan's execution limit.",
    "usage.warning.overLimitMessage": "You have exceeded your plan's execution limit.",
    "usage.warning.resetDate": "Usage resets on",
    "usage.warning.upgradePlan": "Upgrade Plan",
    "usage.warning.whatHappens": "What happens when you reach the limit?",
    "usage.warning.whatNow": "What can I do?",

    # workflow
    "workflow.addDescription": "Add Description",
    "workflow.collapse": "Collapse",
    "workflow.collapseNode": "Collapse Node",
    "workflow.descriptionHint": "Describe what this workflow does",
    "workflow.descriptionPlaceholder": "Enter workflow description...",
    "workflow.descriptionRemoved": "Description removed",
    "workflow.descriptionSaveShortcut": "Ctrl+Enter to save",
    "workflow.descriptionSaved": "Description saved",
    "workflow.editDescription": "Edit Description",
    "workflow.expand": "Expand",
    "workflow.expandNode": "Expand Node",
    "workflow.insertNode": "Insert Node",
    "workflow.insertNode.subtitle": "Add a new node between existing connections",
    "workflow.insertNode.title": "Insert Node",
    "workflow.pinRequiresOutput": "Pin requires at least one output connection",
    "workflow.replaceNode.subtitle": "Replace this node with a different one",
    "workflow.replaceNode.title": "Replace Node",
    "workflow.validation.apiError": "API validation error",

    # workflowCanvas
    "workflowCanvas.stickyNoteCreated": "Sticky note created",
}

fixed = 0
for f in sorted(CLOUD_EN.rglob('*.json')):
    with open(f, encoding='utf-8') as fh:
        data = json.load(fh)

    changed = False
    for k, v in data.get('translations', {}).items():
        if v == '':
            if k in MANUAL:
                data['translations'][k] = MANUAL[k]
                changed = True
                fixed += 1
            else:
                # Auto-generate from key name
                val = key_to_english(k)
                data['translations'][k] = val
                changed = True
                fixed += 1

    if changed:
        with open(f, 'w', encoding='utf-8') as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
            fh.write('\n')

print(f'Fixed {fixed} empty values')

# Verify no empty left
remaining = 0
for f in sorted(CLOUD_EN.rglob('*.json')):
    with open(f, encoding='utf-8') as fh:
        data = json.load(fh)
    for v in data.get('translations', {}).values():
        if v == '':
            remaining += 1
print(f'Remaining empty: {remaining}')

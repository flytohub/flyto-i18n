"""The settings UI must distinguish the saved source, readiness and planner host."""
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    'aiSourceTitle', 'aiSourceDescription', 'aiSourceApi', 'aiSourceCodex', 'aiSourceClaude',
    'aiSourceSaved', 'aiSourcePending', 'aiSourceReady', 'aiSourceNeedsLogin',
    'aiSourceUnavailable', 'aiSourceNotInstalled', 'aiSourceNotSupported', 'aiSourceLoadError',
    'aiSourceNoFallback', 'aiSourcePrivacy', 'aiSourceUsePlanner', 'aiSourcePlannerHint',
    'aiSourcePlannerError', 'aiSourceSaveSuccess', 'aiSourceSaveError',
    'aiAdvanced', 'aiApiKey', 'aiApiKeyHint', 'aiAssistantDesc', 'aiAutoExecute',
    'aiAutoExecuteDesc', 'aiAutoImport', 'aiAutoImportDesc', 'aiBaseUrl', 'aiBehavior',
    'aiConfigured', 'aiCreative', 'aiMaxTokens', 'aiModel', 'aiModelDefault',
    'aiModelsAvailable', 'aiPrecise', 'aiProvider', 'aiSaveSuccess', 'aiTemperature',
    'aiTestConnection', 'aiTesting',
)


@pytest.mark.parametrize('locale', ['en', 'zh-TW', 'zh-CN'])
def test_source_readiness_and_existing_api_labels_are_reviewed_and_bundled(locale):
    """Pin complete reviewed settings copy in each shipped baseline locale."""
    source = json.loads((ROOT / f'locales/cloud/{locale}/userSettings.json').read_text())['translations']
    cloud = json.loads((ROOT / f'dist/cloud/{locale}.json').read_text())['translations']
    aggregate = json.loads((ROOT / f'dist/{locale}.json').read_text())['translations']
    for suffix in REQUIRED:
        key = 'userSettings.' + suffix
        value = source[key]
        assert isinstance(value, str) and value.strip()
        assert not value.startswith('Ai '), key
        assert cloud['userSettings'][suffix] == value
        assert aggregate['userSettings'][suffix] == value
        if locale != 'en' and suffix not in ('aiSourceCodex', 'aiSourceClaude'):
            assert any('\u3400' <= char <= '\u9fff' for char in value), key

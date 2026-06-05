from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# -----------------------------
# CONFIG (UPDATED FOR SYDNEY)
# -----------------------------
WATSONX_URL = "https://au-syd.ml.cloud.ibm.com"
API_KEY = "API_KEY"
PROJECT_ID = "PROJECT_ID"

print("\n--- [WATSONX CONNECTION INITIALIZING] ---")
print(f"[*] Target Regional URL   : {WATSONX_URL}")
print(f"[*] Project Environment ID : {PROJECT_ID}")
print("-----------------------------------------\n")

# -----------------------------
# CLIENT OPTION
# -----------------------------
def get_watsonx_client():
    """Initializes and returns the authenticated core SDK client layer."""
    credentials = Credentials(
        url=WATSONX_URL,
        api_key=API_KEY
    )
    client = APIClient(credentials)
    client.set.default_project(PROJECT_ID)
    return client

# -----------------------------
# GRANITE MODEL
# -----------------------------
def get_granite_model():
    """Initializes the IBM Granite foundation model inference wrapper."""
    credentials = Credentials(
        url=WATSONX_URL,
        api_key=API_KEY
    )

    params = {
        GenParams.DECODING_METHOD: "sample",
        GenParams.MAX_NEW_TOKENS: 1000,
        GenParams.TEMPERATURE: 0.7,
        GenParams.REPETITION_PENALTY: 1.1,
    }

    model = ModelInference(
        model_id="ibm/granite-3-3-8b-instruct",
        credentials=credentials,
        project_id=PROJECT_ID,
        params=params
    )

    return model

# -----------------------------
# SHARED INSTANCES
# -----------------------------
try:
    watsonx_client = get_watsonx_client()
    granite_model = get_granite_model()
    print("[+] watsonx.ai client modules successfully instantiated in Sydney.\n")
except Exception as e:
    print(f"[!] Initialization error: {e}")
    raise e
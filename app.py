import streamlit as st
from watsonx_client import granite_model  # Imports your pre-configured connection instance

# 1. Page Configuration & Styling
st.set_page_config(
    page_title="AI Recipe Preparation Agent",
    page_icon="🍳",
    layout="centered"
)

# Render Header Title & Subtext
st.title("🍳 AI Recipe Preparation Agent")
st.caption("Powered by IBM Granite-3.3-8b & watsonx.ai")
st.write("Generate personalized recipes based on available ingredients, preferred cuisine, and dietary requirements.")

st.markdown("---")

# 2. Main Form Input Elements
# 🍽️ Select Cuisine
cuisine = st.selectbox(
    "🍽️ Select Cuisine",
    ["Indian", "Italian", "Mexican", "Continental", "Asian", "Mediterranean"]
)

# 🥗 Diet Preference
diet = st.radio(
    "🥗 Diet Preference",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

# 👥 Number of Servings (Slider from 1 to 10)
servings = st.slider(
    "👥 Number of Servings",
    min_value=1,
    max_value=10,
    value=1
)

# ⏱️ Maximum Cooking Time
cooking_time = st.select_slider(
    "⏱️ Maximum Cooking Time",
    options=["5 mins", "15 mins", "30 mins", "45 mins", "60 mins+"],
    value="15 mins"
)

# 🛒 Enter Available Ingredients
ingredients = st.text_area(
    "🛒 Enter Available Ingredients",
    placeholder="e.g., Potato, Paneer, Tomato, Ginger, Spinach"
)

st.markdown("---")

# 3. Execution Action Trigger
if st.button("GENERATE RECIPE", type="primary"):
    
    if not ingredients.strip():
        st.warning("Please input at least one ingredient to help your digital sous-chef get started!")
    else:
        with st.spinner("🤖 Chef Agent is brainstorming ideas and generating your recipe..."):
            
            # Formulate structural system instructions for the LLM execution wrapper
            system_prompt = (
                f"You are an expert digital chef. Generate a precise, delicious recipe using these custom parameters:\n"
                f"- Cuisine style: {cuisine}\n"
                f"- Diet constraint: {diet}\n"
                f"- Servings required: {servings}\n"
                f"- Maximum cooking duration limit: {cooking_time}\n"
                f"- Available kitchen ingredients: {ingredients}\n\n"
                f"Provide a beautifully structured markdown response containing a Recipe Title, "
                f"Estimated Prep/Cook Time, adjusted Portion Details, Ingredients Checklist, and clear Step-by-Step cooking instructions."
            )
            
            try:
                # Issue direct inference call over to Watson Machine Learning
                output_text = granite_model.generate_text(prompt=system_prompt)
                
                # 4. Render Dynamic Output Box
                st.success("🍽️ Your Personalized Recipe Is Ready!")
                st.markdown(output_text)
                
            except Exception as error:
                st.error("Encountered an issue generating the recipe through IBM watsonx.ai.")
                st.info(f"Technical Exception Details: {error}")

# Footer Meta branding elements
st.markdown("---")
st.caption("Built using Streamlit • IBM Cloud • watsonx.ai • Granite Foundation Models")
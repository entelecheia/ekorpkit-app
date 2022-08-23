import streamlit as st
from backend import ServiceError, imagine_from_backend, get_version


backend_url = st.secrets["BACKEND_SERVER"]

st.title("ekorpkit-app: Disco Diffusion Simulator")
st.header("Generate images from text")


text_prompts = st.text_input(
    "What do you want to see?", "Beautiful photorealistic rendering of Jeju Island."
)
init_image = st.file_uploader("Choose an image")
steps = st.slider("Number of diffusion steps", 25, 1000, 250)


if st.button("Imagine!") and len(text_prompts) > 0:
    container = st.empty()
    container.markdown(
        f"""
        <style> p {{ margin:0 }} div {{ margin:0 }} </style>
        <div data-stale="false" class="element-container">
        <div class="stAlert">
        <div data-testid="stMarkdownContainer">
                <img src="https://raw.githubusercontent.com/entelecheia/ekorpkit-app/main/assets/loading.gif" width="30"/>
                Imagining for: <b>{text_prompts}</b>
        </div>
        </div>
        </div>
        <small><i>Imagining may take up to 10mn. Please stand by.</i></small>
    """,
        unsafe_allow_html=True,
    )

    try:
        response = imagine_from_backend(backend_url, text_prompts, steps)
        selected = response["images"]
        version = response["version"]

        margin = 0.1  # for better position of zoom in arrow
        n_columns = 3
        cols = st.columns([1] + [margin, 1] * (n_columns - 1))
        for i, img in enumerate(selected):
            cols[(i % n_columns) * 2].image(img)
        container.markdown(f"**{text_prompts}**")

        st.button("Imagine again!", key="again_button")

    except ServiceError as error:
        container.text(f"Service unavailable, status: {error.status_code}")
    except KeyError:
        container.markdown("Please try again or [report it](mailto:yj.lee@chu.ac.kr).")

st.write(
    f"<small><center>version: {get_version(backend_url)}</center></small>",
    unsafe_allow_html=True,
)

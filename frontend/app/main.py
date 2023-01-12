import streamlit as st
from PIL import Image
from backend import ServiceError, imagine_from_backend, get_version


backend_url = st.secrets["BACKEND_SERVER"]

st.title("Stable Diffusion Simulator")
st.header("Generate images from text")


text_prompts = st.text_input(
    "What do you want to see?", "Beautiful photorealistic rendering of Jeju Island."
)

num_samples = st.slider("Number of samples", 1, 4, 1)
num_inference_steps = st.slider("Number of inference steps", 25, 1000, 100)

uploaded_file = st.file_uploader("Choose an initial image")
if uploaded_file is not None:
    # src_image = load_image(uploaded_file)
    init_image = Image.open(uploaded_file)

    st.image(uploaded_file, caption="Inital image", use_column_width=True)
else:
    init_image = None


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
        response = imagine_from_backend(
            backend_url, text_prompts, num_inference_steps, num_samples, init_image
        )
        images = response.pop("images", [])

        margin = 0.1  # for better position of zoom in arrow
        n_columns = min(num_samples, 2)
        cols = st.columns([1] + [margin, 1] * (n_columns - 1))
        for i, img in enumerate(images):
            cols[(i % n_columns) * 2].image(img)
        container.markdown(f"**{text_prompts}**")
        st.json(response)

    except ServiceError as error:
        container.text(f"Service unavailable, status: {error.status_code}")
    except KeyError:
        container.markdown("Please try again or [report it](mailto:yj.lee@chu.ac.kr).")

st.write(
    f"<small><center>version: {get_version(backend_url)}</center></small>",
    unsafe_allow_html=True,
)

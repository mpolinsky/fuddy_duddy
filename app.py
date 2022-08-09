import streamlit as st
import streamlit.components.v1 as components

st.button(label = "Tweet", components.html("""<a class='twitter-share-button'
			href='https://twitter.com/intent/tweet'
			data-text="Wello Hurld"
			data-url='https://streamlit.io'
			data-show-count='false'>Tweet Here</a>
			<script src='https://platform.twitter.com/widgets.js' charset='utf-8'></script>
			""")
	 )

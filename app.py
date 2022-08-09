import streamlit as st
import streamlit.components.v1 as components


components.html("""<a class='twitter-share-button'
				href='https://twitter.com/intent/tweet'
				data-text=st.session_state.anagram
				data-url='https://streamlit.io'
				data-show-count='false'>
				data-size='Large'
				data-hashtags='streamlit,python'</a>
				<script src='https://platform.twitter.com/widgets.js' charset='utf-8'></script>
				""")

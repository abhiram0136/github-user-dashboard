import streamlit as st
import pandas as pd
from API_PROJECT import get_git_user_data
from DATABASE_PROJECT import(create_table_github,insert_github_info,show_user_info)
create_table_github()
st.title("GIT HUB PORTFOLIO")
username=st.text_input("Enter username of Github")
if st.button("submit"):
    data=get_git_user_data(username)
    if data:
        user_info={
            "username":data["login"],
            "Name":data["name"],
            "Bio":data["bio"],
            "Location":data["location"],
            "Company":data["company"],
            "Followers":data["followers"],
            "Following":data["following"],
            "Profile URL":data["html_url"],
            "Public Repositories" :data["public_repos"],
            "Account created":data["created_at"]
        }

        df=pd.DataFrame(
            list(user_info.items()),
            columns=["Attribute","Value"]
        )
        left_col,right_col=st.columns([1,2])
        with left_col:
            st.image(
                data["avatar_url"],
                width=200,
                caption=data["login"]
            )
            st.link_button(
                "🔗 Visit  Github Profile  ",
                data["html_url"]
            )
        with right_col:
            st.subheader(
                data["name"]
                if data["name"] else data["login"]
            )
            st.write(
                data["bio"]
                if data["bio"] else "No bio available"
            )
            col1,col2,col3=st.columns(3)
            with col1:
                st.metric(
                    label="Followers",
                    value=data["followers"]
                )
            with col2:
                st.metric(
                    label="Following",
                    value=data["following"]
                )
            with col3:
                st.metric(
                    label="Repositories",
                    value=data["public_repos"]
                )
        st.divider()
        tab1,tab2=st.tabs(
            ["📋 User Details", "🗂️ Raw JSON"]
        )
        with tab1:
            st.subheader(
                "Processed User information"
            )
            st.dataframe(
                df,
                use_container_width=True
            )
        with tab2:
            st.subheader("Complete API response")
            st.json(data)
        insert_github_info(
            data['login'],
            data['name'],
            data['followers'],
            data['following'],
            data['public_repos']

        )
    else:
        st.error("" \
        "User not found")

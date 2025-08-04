
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SearchField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class aitoolsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=250)])
    url = StringField('Url', validators=[DataRequired(), Length(min=2, max=250)])
    category = SelectField('Category', choices=[('dev-tools', 'dev-tools'),
                                               ('Ai-tools', 'Ai-tools'), 
                                               ('productivity-tools', 'productivity-tools'), 
                                               ('generative-ai', 'generative-ai'), 
                                               ('machine-learning', 'machine-learning'), 
                                               ('knowledge-base', 'knowledge-base'), 
                                               ('api', 'api'),
                                               ('data', 'data'),
                                               ('data-visualization', 'data-visualization'),
                                               ('data-science', 'data-science'),
                                               ('data-analytics', 'data-analytics'),
                                               ('data-mining', 'data-mining'),
                                               ('career', 'career'),
                                               ('Business', 'Business'),
                                               ('SaaS', 'SaaS'),
                                               ('cyber-security', 'cyber-security'),
                                               ('ai-bots', 'ai-bots'),
                                               ('science', 'science'),  
                                               ('faith', 'faith'),     
                                               ('health&fitness', 'health&fitness'),
                                               ('education', 'education'),
                                               ('technology', 'technology'),
                                               ('react', 'react'),
                                               ('ai-news', 'ai-news'),
                                               ('culture', 'culture'),
                                               ('community', 'community'),
                                               ('Breaking-news', 'Breaking-News'),
                                               ('podcast', 'podcast'),
                                               ('robotics', 'robotics'),
                                               ('research', 'research'),
                                               ('research-tools', 'research-tools'),
                                               ('value-addition', 'value-addition'),
                                               ('SEO', 'SEO'),
                                               ('branding', 'branding'),
                                               ('marketing', 'marketing')
                                               ])



    submit = SubmitField('Add Tools')


 
    

class updateForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired(), Length(min=2, max=250)])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=250)])
    url = StringField('Url', validators=[DataRequired(), Length(min=2, max=250)])
    category = SelectField('Category', choices=[('dev-tools', 'dev-tools'),
                                               ('Ai-tools', 'Ai-tools'), 
                                               ('productivity-tools', 'productivity-tools'), 
                                               ('generative-ai', 'generative-ai'), 
                                               ('machine-learning', 'machine-learning'), 
                                               ('knowledge-base', 'knowledge-base'),
                                               ('api', 'api'),
                                               ('data', 'data'),
                                               ('data-visualization', 'data-visualization'),
                                               ('data-science', 'data-science'),
                                               ('data-analytics', 'data-analytics'),
                                               ('data-mining', 'data-mining'),
                                               ('career', 'career'),
                                               ('Business', 'Business'),
                                               ('SaaS', 'Saas'),
                                               ('cyber-security', 'cyber-security'),
                                               ('ai-bots', 'ai-bots'),
                                               ('science', 'science'),
                                               ('faith', 'faith'),
                                               ('health&fitness', 'health&fitness'),
                                               ('education', 'education'),
                                               ('technology', 'technology'),
                                               ('react', 'react'),
                                               ('ai-news', 'ai-news'),
                                               ('culture', 'culture'),
                                               ('community', 'community'),
                                               ('Breaking-news', 'Breaking-News'),
                                               ('podcast', 'podcast'),
                                               ('robotics', 'robotics'),
                                               ('research', 'research'),
                                               ('research-tools', 'research-tools'),
                                               ('value-addition', 'value-addition'),
                                               ('SEO', 'SEO'),
                                               ('social-media', 'social-media'),
                                               ('marketing', 'marketing')
                                               ])
    
    submit = SubmitField('Update Tools')



class adduserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=250)])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=250)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=250)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Add User')
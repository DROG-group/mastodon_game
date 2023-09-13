# app/services/world_service.py

from app.models import World, Story, Bot
from app.prompts import story_prompts, interaction_prompts
from app.services.openai_api import generate_content

def build_world():
    # Generate main story arc
    main_arc_prompt = story_prompts.MAIN_ARC_PROMPT
    main_arc = generate_content(main_arc_prompt)
    
    # Create or update the main story arc in the World model
    world = World.query.first()
    if not world:
        world = World(arc=main_arc)
        world.save()
    else:
        world.arc = main_arc
        world.update()

    # Generate subplots or events
    for subplot_prompt in story_prompts.SUBPLOT_PROMPTS:
        subplot = generate_content(subplot_prompt)
        
        # Save subplot to the Story model
        story = Story(content=subplot, world_id=world.id)
        story.save()

        # Generate bot interactions for each subplot
        interaction_prompt = interaction_prompts.get_interaction_prompt(subplot)
        for _ in range(5):  # Generate 5 interactions for each subplot
            interaction = generate_content(interaction_prompt)
            
            # Create a bot to represent this interaction
            bot = Bot(content=interaction, story_id=story.id)
            bot.save()

    return world

# ... (other service functions related to world-building)

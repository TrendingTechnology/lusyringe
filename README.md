<div align="center">
  <img src=".media/medical-care.svg" alt="drawing" width="500" />

  <h1 align="center">
    LuSyringe
  </h1>
</div>

<div align="center">
  LuSyringe is a documentation injection tool for your classes when using 
  
  <a href="https://fastapi.tiangolo.com">
    <code>Fast API</code>
  </a>

&nbsp;

</div>

## Benefits

The main benefit is being able to separate your business code (classes) from the logic of the documentation and pydantic validation. For example, a class that serves as a response for an endpoint may look like this without LuSyringe:

```py
class HealthResponse(BaseModel):
  ping: str = Field(..., example="pong")
  version: str = Field(..., example="1.0.0")
```

And that's not bad at first look, but the response class is tightly coupled of the logic of the validation + documentation offered by Pydantic and FastAPI. When dealing with inheritance, you may run into cases that the search for where the documentation is being defined is a bit harsh.

Well, with LuSyringe that's how the `HealthReponse` class would look.

```py
from lusyringe import lusyringe

class HealthResponse(metaclass=lusyringe(health_response_docs)):
  ping: str
  version: str
```

Nice, isn't it? 🤩. But hey, what about inheritance, what if I'm inheriting these fields from a base class, or what if this base class is inheriting these fields?

Hey, calm down. I solved all these things for you here, no need to worries 😝, ah! I do type checking for you too, (but I also have a non-strict mode if you are adventurous)
.

## How it works

The usage is pretty simple 🥰. You can define your docs object in the following manner:

```py
from lusyringe import Prescription

health_response_docs = [
    Prescription(
        field='ping',
        type=str,
        doc=Field(..., example='Pong')
    ),
    Prescription(
        field='version',
        type=str,
        doc=Field(..., example='0.0.1')
    ),
]

```

Then you can pass your docs object to lusyringe, like this:

```py
from lusyringe import lusyringe

# import your file
from ... import health_response_docs

class HealthResponse(metaclass=lusyringe(health_response_docs)):
  ping: str
  version: str
```

Cool, huh? I can throw some errors if you forget to define your fields in the class, or in a base class being inherited from 👮

```py
NotImplementedError: f"Documentation for {field} with type {type_} was found,"
                     f"but field was not implemented in {class_name}"
```

So be a good developer and do not forget to declare your things. But hey! Remember when I called you adventurous? Yeah, I have a little surprise for you:

```py
class HealthResponse(metaclass=lusyringe(health_response_docs, strict=False)):
  pass
```

What!? What does the strict mean? Well, basically I'll allow your recklessness in don't defining the fields, so I'll do it for you 🙄. But I'll get mad if you declare something with the wrong type! So be in line.

```py
ValueError: f"Tried to apply type {applied_type} to already defined {field}"
            f"of another type"
```

## Installing

Initially this will only be available for the folks at Luizalabs 😇. But if you are from here, you can just:

```sh
pip install lusyringe
```

If you have our pypi

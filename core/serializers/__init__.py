from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraSerializer,
    ItensCompraSerializer,
    CompraListSerializer,
    ItensCompraListSerializer,
    CompraCreateUpdateSerializer,
    ItensCompraCreateUpdateSerializer,
)
from .editora import EditoraSerializer
from .livro import (
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
from .user import UserRegistrationSerializer, UserSerializer

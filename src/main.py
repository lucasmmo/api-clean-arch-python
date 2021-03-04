from adapters.repositories.UserRepository import UserRepository
from domain.entities.User import User

from adapters.controllers.SaveUserController import SaveUserController
from adapters.controllers.LoadUserController import LoadUserController
from adapters.controllers.DeleteUserController import DeleteUserController

from domain.interactors.users.SaveUserInteractor import SaveUserInteractor
from domain.interactors.users.LoadUserInteractor import LoadUserInteractor
from domain.interactors.users.DeleteUserInteractor import DeleteUserInteractor

mUser = User(1, "lucas", "monteiro", 19, "lucas@gmail.com", "12345", False, "hoje", "hoje") 
mRepository = UserRepository()

mInteractorSave = SaveUserInteractor(mRepository)
mControllerSave = SaveUserController(mInteractorSave, mUser)

mInteractorLoad = LoadUserInteractor(mRepository)
mControllerLoad = LoadUserController(mInteractorLoad, mUser.user_id)

mInteractorDelete = DeleteUserInteractor(mRepository)
mControllerDelete = DeleteUserController(mInteractorDelete, mUser.user_id)

mControllerSave.handle()

print(mControllerLoad.handle())

print(mControllerDelete.handle())
 
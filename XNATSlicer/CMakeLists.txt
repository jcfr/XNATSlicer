
#-----------------------------------------------------------------------------
set(MODULE_NAME XNATSlicer)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
  ${MODULE_NAME}Lib/__init__.py
  ${MODULE_NAME}Lib/XNATAddProjEditor.py
  ${MODULE_NAME}Lib/XNATBrowser.py
  ${MODULE_NAME}Lib/XNATCommunicator.py
  ${MODULE_NAME}Lib/XNATFileInfo.py
  ${MODULE_NAME}Lib/XNATInstallWizard.py
  ${MODULE_NAME}Lib/XNATLoadWorkflow.py
  ${MODULE_NAME}Lib/XNATMRMLParser.py
  ${MODULE_NAME}Lib/XNATSaveDialog.py
  ${MODULE_NAME}Lib/XNATSaveWorkflow.py
  ${MODULE_NAME}Lib/XNATScenePackager.py
  ${MODULE_NAME}Lib/XNATSessionManager.py
  ${MODULE_NAME}Lib/XNATSettings.py
  ${MODULE_NAME}Lib/XNATTimer.py
  ${MODULE_NAME}Lib/XNATTreeView.py
  ${MODULE_NAME}Lib/XNATUtils.py
  ${MODULE_NAME}Lib/XNATView.py
  )

set(MODULE_PYTHON_RESOURCES
  Resources/Icons/${MODULE_NAME}.png
  ${MODULE_NAME}Lib/data/Utils
  ${MODULE_NAME}Lib/icons/addproj.jpg
  ${MODULE_NAME}Lib/icons/delete.jpg
  ${MODULE_NAME}Lib/icons/load.jpg
  ${MODULE_NAME}Lib/icons/save.jpg
  ${MODULE_NAME}Lib/icons/update.jpg
  ${MODULE_NAME}Lib/icons/wrench.png
  )

#-----------------------------------------------------------------------------
slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS "${MODULE_PYTHON_SCRIPTS}"
  RESOURCES "${MODULE_PYTHON_RESOURCES}"
  )

#-----------------------------------------------------------------------------
if(BUILD_TESTING)

  # this will regiester the unittest subclass in the main script
  # as a ctest (note that it is also usable as a runtime test).
  slicer_add_python_unittest(SCRIPT ${MODULE_NAME}.py)

  # additional build-time testing goes in here
  add_subdirectory(Testing)
endif()


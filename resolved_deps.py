resolved = [
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "/home/node/.cache/bazel/_bazel_node/install/97c81a3bdd984debe0ff1b26c2dc04e0/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository aspect_rules_js instantiated at:\n  /workspaces/repro/WORKSPACE:3:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_js",
               "url": "https://github.com/aspect-build/rules_js/archive/refs/tags/v1.13.0.tar.gz",
               "sha256": "66ecc9f56300dd63fb86f11cfa1e8affcaa42d5300e2746dba08541916e913fd",
               "strip_prefix": "rules_js-1.13.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/aspect-build/rules_js/archive/refs/tags/v1.13.0.tar.gz",
                         "urls": [],
                         "sha256": "66ecc9f56300dd63fb86f11cfa1e8affcaa42d5300e2746dba08541916e913fd",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_js-1.13.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "aspect_rules_js"
                    },
                    "output_tree_hash": "ad2d805448233199c003b082bd28a06ca2002730072e832659c8b3321f529763"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_nodejs instantiated at:\n  /workspaces/repro/WORKSPACE:12:22: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/js/repositories.bzl:18:17: in rules_js_dependencies\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/js/private/maybe.bzl:7:10: in maybe_http_archive\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_nodejs",
               "generator_name": "rules_nodejs",
               "generator_function": "rules_js_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_nodejs/releases/download/5.7.1/rules_nodejs-core-5.7.1.tar.gz"
               ],
               "sha256": "50adf0b0ff6fc77d6909a790df02eefbbb3bc2b154ece3406361dda49607a7bd"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_nodejs/releases/download/5.7.1/rules_nodejs-core-5.7.1.tar.gz"
                         ],
                         "sha256": "50adf0b0ff6fc77d6909a790df02eefbbb3bc2b154ece3406361dda49607a7bd",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_nodejs"
                    },
                    "output_tree_hash": "54ce119d58a68a3be7ea904e1546305541f01320f5b659c24a752856b8a4acf7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_skylib instantiated at:\n  /workspaces/repro/WORKSPACE:12:22: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/js/repositories.bzl:12:17: in rules_js_dependencies\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/js/private/maybe.bzl:7:10: in maybe_http_archive\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_skylib",
               "generator_name": "bazel_skylib",
               "generator_function": "rules_js_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz"
               ],
               "sha256": "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz"
                         ],
                         "sha256": "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_skylib"
                    },
                    "output_tree_hash": "ea7c4298620705f0369110da5db3dec89df5ed43983fc85435f336e5fb95b3f9"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository aspect_bazel_lib instantiated at:\n  /workspaces/repro/WORKSPACE:12:22: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/js/repositories.bzl:24:17: in rules_js_dependencies\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/js/private/maybe.bzl:7:10: in maybe_http_archive\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_bazel_lib",
               "generator_name": "aspect_bazel_lib",
               "generator_function": "rules_js_dependencies",
               "generator_location": None,
               "url": "https://github.com/aspect-build/bazel-lib/archive/refs/tags/v1.18.0.tar.gz",
               "sha256": "be236556c7b9c7b91cb370e837fdcec62b6e8893408cd4465ae883c9d7c67024",
               "strip_prefix": "bazel-lib-1.18.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/aspect-build/bazel-lib/archive/refs/tags/v1.18.0.tar.gz",
                         "urls": [],
                         "sha256": "be236556c7b9c7b91cb370e837fdcec62b6e8893408cd4465ae883c9d7c67024",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "bazel-lib-1.18.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "aspect_bazel_lib"
                    },
                    "output_tree_hash": "76c34a75b3b290f7e0d85b1e7990c03fe6c0468c73b42bf4fb80c930846ab0e9"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm/private:npm_translate_lock.bzl%npm_translate_lock",
          "definition_information": "Repository npm instantiated at:\n  /workspaces/repro/WORKSPACE:23:19: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:382:24: in npm_translate_lock\nRepository rule npm_translate_lock defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/private/npm_translate_lock.bzl:94:37: in <toplevel>\n",
          "original_attributes": {
               "name": "npm",
               "generator_name": "npm",
               "generator_function": "npm_translate_lock",
               "generator_location": None,
               "pnpm_lock": "//:pnpm-lock.yaml",
               "preupdate": [],
               "patches": {},
               "patch_args": {
                    "*": [
                         "-p0"
                    ]
               },
               "custom_postinstalls": {},
               "prod": False,
               "public_hoist_packages": {},
               "dev": False,
               "no_optional": False,
               "lifecycle_hooks": {
                    "*": [
                         "preinstall",
                         "install",
                         "postinstall"
                    ]
               },
               "lifecycle_hooks_envs": {},
               "lifecycle_hooks_execution_requirements": {
                    "*": [
                         "no-sandbox"
                    ]
               },
               "bins": {},
               "verify_node_modules_ignored": "//:.bazelignore",
               "additional_file_contents": {},
               "data": [],
               "quiet": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm/private:npm_translate_lock.bzl%npm_translate_lock",
                    "attributes": {
                         "name": "npm",
                         "generator_name": "npm",
                         "generator_function": "npm_translate_lock",
                         "generator_location": None,
                         "pnpm_lock": "//:pnpm-lock.yaml",
                         "preupdate": [],
                         "patches": {},
                         "patch_args": {
                              "*": [
                                   "-p0"
                              ]
                         },
                         "custom_postinstalls": {},
                         "prod": False,
                         "public_hoist_packages": {},
                         "dev": False,
                         "no_optional": False,
                         "lifecycle_hooks": {
                              "*": [
                                   "preinstall",
                                   "install",
                                   "postinstall"
                              ]
                         },
                         "lifecycle_hooks_envs": {},
                         "lifecycle_hooks_execution_requirements": {
                              "*": [
                                   "no-sandbox"
                              ]
                         },
                         "bins": {},
                         "verify_node_modules_ignored": "//:.bazelignore",
                         "additional_file_contents": {},
                         "data": [],
                         "quiet": True
                    },
                    "output_tree_hash": "40943348db507feaab5537316906ee870f1e512a358cbcb81db62abec4d8017d"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_android-arm64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:24:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_android-arm64__0.16.12__links",
               "generator_name": "npm__at_esbuild_android-arm64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/android-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/android-arm64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_android-arm64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_android-arm64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/android-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/android-arm64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "bcf5fe3b4dc0a43fac0497868b8a8a27ddc3f81c12735e977ac5bb2f9d3f95ed"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_android-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:41:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_android-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_android-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/android-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/android-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_android-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_android-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/android-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/android-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "fa471341ebb2467eeba66471c7604ad7e235c5a0395a43b99591e50f556cb31a"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-ia32__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:160:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-ia32__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-ia32__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-ia32",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-ia32": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-ia32__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-ia32__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-ia32",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-ia32": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "ce284783a1fdd8d657a13534140dcc5b7c7717868af4bba9d40271460c189886"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-arm__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:126:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-arm__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-arm__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-arm",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-arm": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-arm__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-arm__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-arm",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-arm": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "5eccfc33c6f055aafc65b24fc4cd289196678eb1a31eb45f063ddce477132a68"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_freebsd-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:109:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_freebsd-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_freebsd-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/freebsd-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/freebsd-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_freebsd-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_freebsd-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/freebsd-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/freebsd-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "0cb6722b16771c56ecb1592ebb52fa79aa588945c3bbe7e7106af1ec3e4cfe15"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-arm64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:143:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-arm64__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-arm64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-arm64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-arm64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-arm64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-arm64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "6dfe350242a31763041c3ce5fd218fc26a498f80f478b984606f9573a5a6a094"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__source-map-js__1.0.2__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:627:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__source-map-js__1.0.2__links",
               "generator_name": "npm__source-map-js__1.0.2__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "source-map-js",
               "version": "1.0.2",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "source-map-js": [
                         "1.0.2"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__source-map-js__1.0.2__links",
                         "generator_name": "npm__source-map-js__1.0.2__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "source-map-js",
                         "version": "1.0.2",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "source-map-js": [
                                   "1.0.2"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "6c6873e917bc4dbfe8b698a3c8005a3d50b357a147bafb522e2f518c0daed864"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_freebsd-arm64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:92:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_freebsd-arm64__0.16.12__links",
               "generator_name": "npm__at_esbuild_freebsd-arm64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/freebsd-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/freebsd-arm64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_freebsd-arm64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_freebsd-arm64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/freebsd-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/freebsd-arm64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "8944444ed169d57afd63e1c84c6f64e11eff72095534a0b263f6ea926de62fb4"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_netbsd-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:279:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_netbsd-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_netbsd-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/netbsd-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/netbsd-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_netbsd-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_netbsd-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/netbsd-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/netbsd-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "cd498dea5d5a4ed3ab94148724238a955d3cde4ab8734ce49c8dbf3d8e519d3a"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_darwin-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:75:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_darwin-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_darwin-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/darwin-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/darwin-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_darwin-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_darwin-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/darwin-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/darwin-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "4f991e736ec6abe6a14d739176f44e32b17a88556d3b33ea5ff965bce7852658"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__fsevents__2.3.2__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:444:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__fsevents__2.3.2__links",
               "generator_name": "npm__fsevents__2.3.2__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "fsevents",
               "version": "2.3.2",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "fsevents": [
                         "2.3.2"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__fsevents__2.3.2__links",
                         "generator_name": "npm__fsevents__2.3.2__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "fsevents",
                         "version": "2.3.2",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "fsevents": [
                                   "2.3.2"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "984f2b46b20e34faa73985fbe821d49649826e97798aad73fb692890cb238172"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__is-core-module__2.11.0__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:495:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__is-core-module__2.11.0__links",
               "generator_name": "npm__is-core-module__2.11.0__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "is-core-module",
               "version": "2.11.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "has": "1.0.3"
               },
               "transitive_closure": {
                    "is-core-module": [
                         "2.11.0"
                    ],
                    "has": [
                         "1.0.3"
                    ],
                    "function-bind": [
                         "1.1.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__is-core-module__2.11.0__links",
                         "generator_name": "npm__is-core-module__2.11.0__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "is-core-module",
                         "version": "2.11.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "has": "1.0.3"
                         },
                         "transitive_closure": {
                              "is-core-module": [
                                   "2.11.0"
                              ],
                              "has": [
                                   "1.0.3"
                              ],
                              "function-bind": [
                                   "1.1.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "f90557ea424758ecdc7d2480e091d9c20068eb203b66e432229ec37a32b1e168"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__has__1.0.3__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:476:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__has__1.0.3__links",
               "generator_name": "npm__has__1.0.3__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "has",
               "version": "1.0.3",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "function-bind": "1.1.1"
               },
               "transitive_closure": {
                    "has": [
                         "1.0.3"
                    ],
                    "function-bind": [
                         "1.1.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__has__1.0.3__links",
                         "generator_name": "npm__has__1.0.3__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "has",
                         "version": "1.0.3",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "function-bind": "1.1.1"
                         },
                         "transitive_closure": {
                              "has": [
                                   "1.0.3"
                              ],
                              "function-bind": [
                                   "1.1.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "c2fa670fe615639d786605a3f52738388d2e27fdf48013f0c8f9f28182e3002e"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__rollup__3.9.1__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:608:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__rollup__3.9.1__links",
               "generator_name": "npm__rollup__3.9.1__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "rollup",
               "version": "3.9.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "fsevents": "2.3.2"
               },
               "transitive_closure": {
                    "rollup": [
                         "3.9.1"
                    ],
                    "fsevents": [
                         "2.3.2"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__rollup__3.9.1__links",
                         "generator_name": "npm__rollup__3.9.1__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "rollup",
                         "version": "3.9.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "fsevents": "2.3.2"
                         },
                         "transitive_closure": {
                              "rollup": [
                                   "3.9.1"
                              ],
                              "fsevents": [
                                   "2.3.2"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "c93e56da6bfae116a9a674d68f3b443adae5d102048e8a71667c13b9c80a6480"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_win32-ia32__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:347:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_win32-ia32__0.16.12__links",
               "generator_name": "npm__at_esbuild_win32-ia32__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/win32-ia32",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/win32-ia32": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_win32-ia32__0.16.12__links",
                         "generator_name": "npm__at_esbuild_win32-ia32__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/win32-ia32",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/win32-ia32": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "6be2f710b0e8a7358a9556154de12a3631513f3171ebcbb0532b9de74efdf4a2"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__vite__4.0.3__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:657:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__vite__4.0.3__links",
               "generator_name": "npm__vite__4.0.3__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "vite",
               "version": "4.0.3",
               "root_package": "",
               "link_packages": {
                    "": [
                         "vite"
                    ]
               },
               "bins": {},
               "deps": {
                    "fsevents": "2.3.2",
                    "esbuild": "0.16.12",
                    "postcss": "8.4.20",
                    "resolve": "1.22.1",
                    "rollup": "3.9.1"
               },
               "transitive_closure": {
                    "vite": [
                         "4.0.3"
                    ],
                    "esbuild": [
                         "0.16.12"
                    ],
                    "postcss": [
                         "8.4.20"
                    ],
                    "resolve": [
                         "1.22.1"
                    ],
                    "rollup": [
                         "3.9.1"
                    ],
                    "fsevents": [
                         "2.3.2"
                    ],
                    "is-core-module": [
                         "2.11.0"
                    ],
                    "path-parse": [
                         "1.0.7"
                    ],
                    "supports-preserve-symlinks-flag": [
                         "1.0.0"
                    ],
                    "has": [
                         "1.0.3"
                    ],
                    "function-bind": [
                         "1.1.1"
                    ],
                    "nanoid": [
                         "3.3.4"
                    ],
                    "picocolors": [
                         "1.0.0"
                    ],
                    "source-map-js": [
                         "1.0.2"
                    ],
                    "@esbuild/android-arm": [
                         "0.16.12"
                    ],
                    "@esbuild/android-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/android-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/darwin-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/darwin-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/freebsd-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/freebsd-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-arm": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-ia32": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-loong64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-mips64el": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-ppc64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-riscv64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-s390x": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/netbsd-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/openbsd-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/sunos-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/win32-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/win32-ia32": [
                         "0.16.12"
                    ],
                    "@esbuild/win32-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__vite__4.0.3__links",
                         "generator_name": "npm__vite__4.0.3__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "vite",
                         "version": "4.0.3",
                         "root_package": "",
                         "link_packages": {
                              "": [
                                   "vite"
                              ]
                         },
                         "bins": {},
                         "deps": {
                              "fsevents": "2.3.2",
                              "esbuild": "0.16.12",
                              "postcss": "8.4.20",
                              "resolve": "1.22.1",
                              "rollup": "3.9.1"
                         },
                         "transitive_closure": {
                              "vite": [
                                   "4.0.3"
                              ],
                              "esbuild": [
                                   "0.16.12"
                              ],
                              "postcss": [
                                   "8.4.20"
                              ],
                              "resolve": [
                                   "1.22.1"
                              ],
                              "rollup": [
                                   "3.9.1"
                              ],
                              "fsevents": [
                                   "2.3.2"
                              ],
                              "is-core-module": [
                                   "2.11.0"
                              ],
                              "path-parse": [
                                   "1.0.7"
                              ],
                              "supports-preserve-symlinks-flag": [
                                   "1.0.0"
                              ],
                              "has": [
                                   "1.0.3"
                              ],
                              "function-bind": [
                                   "1.1.1"
                              ],
                              "nanoid": [
                                   "3.3.4"
                              ],
                              "picocolors": [
                                   "1.0.0"
                              ],
                              "source-map-js": [
                                   "1.0.2"
                              ],
                              "@esbuild/android-arm": [
                                   "0.16.12"
                              ],
                              "@esbuild/android-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/android-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/darwin-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/darwin-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/freebsd-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/freebsd-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-arm": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-ia32": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-loong64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-mips64el": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-ppc64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-riscv64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-s390x": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/netbsd-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/openbsd-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/sunos-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/win32-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/win32-ia32": [
                                   "0.16.12"
                              ],
                              "@esbuild/win32-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "49a42449bbe20d297d04c566d115b36f24af5b1407eaa83868e3417c32ec14f3"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-mips64el__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:194:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-mips64el__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-mips64el__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-mips64el",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-mips64el": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-mips64el__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-mips64el__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-mips64el",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-mips64el": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "9fa43171065a7308751fa436a16a6b3feb70459daaa71fdea38fe8908eca7400"
               }
          ]
     },
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__nanoid__3.3.4__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:515:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__nanoid__3.3.4__links",
               "generator_name": "npm__nanoid__3.3.4__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "nanoid",
               "version": "3.3.4",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "nanoid": [
                         "3.3.4"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__nanoid__3.3.4__links",
                         "generator_name": "npm__nanoid__3.3.4__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "nanoid",
                         "version": "3.3.4",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "nanoid": [
                                   "3.3.4"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "03e2ece00aa6ea20f596418be9999acd0cc58a8bec677b8e0723174d64f642b3"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_win32-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:364:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_win32-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_win32-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/win32-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/win32-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_win32-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_win32-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/win32-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/win32-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "0e35fccb1f5cd9463bca530a74d49b938da63b244eb920d37c96313ad48c6877"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_win32-arm64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:330:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_win32-arm64__0.16.12__links",
               "generator_name": "npm__at_esbuild_win32-arm64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/win32-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/win32-arm64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_win32-arm64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_win32-arm64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/win32-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/win32-arm64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "5d7c0d652dbb4cc4483aa23c30172b5302ec48c2fc963a86e90dbd16b43e1b7f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_sunos-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:313:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_sunos-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_sunos-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/sunos-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/sunos-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_sunos-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_sunos-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/sunos-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/sunos-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "6f94bb3d31602e3789f6fed80e0c42f732abd4889b1212bcc34d6240f1fda408"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__postcss__8.4.20__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:560:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__postcss__8.4.20__links",
               "generator_name": "npm__postcss__8.4.20__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "postcss",
               "version": "8.4.20",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "nanoid": "3.3.4",
                    "picocolors": "1.0.0",
                    "source-map-js": "1.0.2"
               },
               "transitive_closure": {
                    "postcss": [
                         "8.4.20"
                    ],
                    "nanoid": [
                         "3.3.4"
                    ],
                    "picocolors": [
                         "1.0.0"
                    ],
                    "source-map-js": [
                         "1.0.2"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__postcss__8.4.20__links",
                         "generator_name": "npm__postcss__8.4.20__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "postcss",
                         "version": "8.4.20",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "nanoid": "3.3.4",
                              "picocolors": "1.0.0",
                              "source-map-js": "1.0.2"
                         },
                         "transitive_closure": {
                              "postcss": [
                                   "8.4.20"
                              ],
                              "nanoid": [
                                   "3.3.4"
                              ],
                              "picocolors": [
                                   "1.0.0"
                              ],
                              "source-map-js": [
                                   "1.0.2"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "7d4cac21d34d9fc437da75940c0ce7d65f63b24cd6d701e07a4ec85ef6d15af6"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-loong64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:177:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-loong64__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-loong64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-loong64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-loong64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-loong64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-loong64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-loong64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-loong64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "4055283961efda269833847a5d9ff45d3f86077cbe5ebf027e84cf86339ec741"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-ppc64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:211:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-ppc64__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-ppc64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-ppc64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-ppc64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-ppc64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-ppc64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-ppc64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-ppc64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "37fb31d11371460e873ac364220869a7fa1ccf1f5f25c48249d40287ff571af7"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__picocolors__1.0.0__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:545:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__picocolors__1.0.0__links",
               "generator_name": "npm__picocolors__1.0.0__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "picocolors",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "picocolors": [
                         "1.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__picocolors__1.0.0__links",
                         "generator_name": "npm__picocolors__1.0.0__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "picocolors",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "picocolors": [
                                   "1.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "2c008db2f1ceac7c31c61fcb0c9ad807aed9ce5ef65e2235073ead666b312ba5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__resolve__1.22.1__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:583:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__resolve__1.22.1__links",
               "generator_name": "npm__resolve__1.22.1__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "resolve",
               "version": "1.22.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "is-core-module": "2.11.0",
                    "path-parse": "1.0.7",
                    "supports-preserve-symlinks-flag": "1.0.0"
               },
               "transitive_closure": {
                    "resolve": [
                         "1.22.1"
                    ],
                    "is-core-module": [
                         "2.11.0"
                    ],
                    "path-parse": [
                         "1.0.7"
                    ],
                    "supports-preserve-symlinks-flag": [
                         "1.0.0"
                    ],
                    "has": [
                         "1.0.3"
                    ],
                    "function-bind": [
                         "1.1.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__resolve__1.22.1__links",
                         "generator_name": "npm__resolve__1.22.1__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "resolve",
                         "version": "1.22.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "is-core-module": "2.11.0",
                              "path-parse": "1.0.7",
                              "supports-preserve-symlinks-flag": "1.0.0"
                         },
                         "transitive_closure": {
                              "resolve": [
                                   "1.22.1"
                              ],
                              "is-core-module": [
                                   "2.11.0"
                              ],
                              "path-parse": [
                                   "1.0.7"
                              ],
                              "supports-preserve-symlinks-flag": [
                                   "1.0.0"
                              ],
                              "has": [
                                   "1.0.3"
                              ],
                              "function-bind": [
                                   "1.1.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "099be1b0ab390af8103d12004c21d26cb7cb399056cdcc361e6f857d63646799"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_darwin-arm64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:58:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_darwin-arm64__0.16.12__links",
               "generator_name": "npm__at_esbuild_darwin-arm64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/darwin-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/darwin-arm64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_darwin-arm64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_darwin-arm64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/darwin-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/darwin-arm64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "541c2ccc91557284bb02d29c0ec1b6ed662a1c36622d838b457cd17ad6b8886d"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_openbsd-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:296:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_openbsd-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_openbsd-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/openbsd-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/openbsd-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_openbsd-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_openbsd-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/openbsd-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/openbsd-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "640d08b4e277ce336fe416029c100e78054fa43e3bfe44f8e3594108da5800b0"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__function-bind__1.1.1__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:461:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__function-bind__1.1.1__links",
               "generator_name": "npm__function-bind__1.1.1__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "function-bind",
               "version": "1.1.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "function-bind": [
                         "1.1.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__function-bind__1.1.1__links",
                         "generator_name": "npm__function-bind__1.1.1__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "function-bind",
                         "version": "1.1.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "function-bind": [
                                   "1.1.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "32396e4c36de96ea04108b9cf4ca6ffa5f58f09b83f4b2c6892182323b1127bb"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__supports-preserve-symlinks-flag__1.0.0__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:642:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__supports-preserve-symlinks-flag__1.0.0__links",
               "generator_name": "npm__supports-preserve-symlinks-flag__1.0.0__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "supports-preserve-symlinks-flag",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "supports-preserve-symlinks-flag": [
                         "1.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__supports-preserve-symlinks-flag__1.0.0__links",
                         "generator_name": "npm__supports-preserve-symlinks-flag__1.0.0__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "supports-preserve-symlinks-flag",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "supports-preserve-symlinks-flag": [
                                   "1.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "e58c9e10037cc4aecf8e24b38b4317582af42fb43bf63e5983421a496f97a38b"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__esbuild__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:381:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__esbuild__0.16.12__links",
               "generator_name": "npm__esbuild__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "esbuild",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "@esbuild/android-arm": "0.16.12",
                    "@esbuild/android-arm64": "0.16.12",
                    "@esbuild/android-x64": "0.16.12",
                    "@esbuild/darwin-arm64": "0.16.12",
                    "@esbuild/darwin-x64": "0.16.12",
                    "@esbuild/freebsd-arm64": "0.16.12",
                    "@esbuild/freebsd-x64": "0.16.12",
                    "@esbuild/linux-arm": "0.16.12",
                    "@esbuild/linux-arm64": "0.16.12",
                    "@esbuild/linux-ia32": "0.16.12",
                    "@esbuild/linux-loong64": "0.16.12",
                    "@esbuild/linux-mips64el": "0.16.12",
                    "@esbuild/linux-ppc64": "0.16.12",
                    "@esbuild/linux-riscv64": "0.16.12",
                    "@esbuild/linux-s390x": "0.16.12",
                    "@esbuild/linux-x64": "0.16.12",
                    "@esbuild/netbsd-x64": "0.16.12",
                    "@esbuild/openbsd-x64": "0.16.12",
                    "@esbuild/sunos-x64": "0.16.12",
                    "@esbuild/win32-arm64": "0.16.12",
                    "@esbuild/win32-ia32": "0.16.12",
                    "@esbuild/win32-x64": "0.16.12"
               },
               "transitive_closure": {
                    "esbuild": [
                         "0.16.12"
                    ],
                    "@esbuild/android-arm": [
                         "0.16.12"
                    ],
                    "@esbuild/android-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/android-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/darwin-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/darwin-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/freebsd-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/freebsd-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-arm": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-ia32": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-loong64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-mips64el": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-ppc64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-riscv64": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-s390x": [
                         "0.16.12"
                    ],
                    "@esbuild/linux-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/netbsd-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/openbsd-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/sunos-x64": [
                         "0.16.12"
                    ],
                    "@esbuild/win32-arm64": [
                         "0.16.12"
                    ],
                    "@esbuild/win32-ia32": [
                         "0.16.12"
                    ],
                    "@esbuild/win32-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__esbuild__0.16.12__links",
                         "generator_name": "npm__esbuild__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "esbuild",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "@esbuild/android-arm": "0.16.12",
                              "@esbuild/android-arm64": "0.16.12",
                              "@esbuild/android-x64": "0.16.12",
                              "@esbuild/darwin-arm64": "0.16.12",
                              "@esbuild/darwin-x64": "0.16.12",
                              "@esbuild/freebsd-arm64": "0.16.12",
                              "@esbuild/freebsd-x64": "0.16.12",
                              "@esbuild/linux-arm": "0.16.12",
                              "@esbuild/linux-arm64": "0.16.12",
                              "@esbuild/linux-ia32": "0.16.12",
                              "@esbuild/linux-loong64": "0.16.12",
                              "@esbuild/linux-mips64el": "0.16.12",
                              "@esbuild/linux-ppc64": "0.16.12",
                              "@esbuild/linux-riscv64": "0.16.12",
                              "@esbuild/linux-s390x": "0.16.12",
                              "@esbuild/linux-x64": "0.16.12",
                              "@esbuild/netbsd-x64": "0.16.12",
                              "@esbuild/openbsd-x64": "0.16.12",
                              "@esbuild/sunos-x64": "0.16.12",
                              "@esbuild/win32-arm64": "0.16.12",
                              "@esbuild/win32-ia32": "0.16.12",
                              "@esbuild/win32-x64": "0.16.12"
                         },
                         "transitive_closure": {
                              "esbuild": [
                                   "0.16.12"
                              ],
                              "@esbuild/android-arm": [
                                   "0.16.12"
                              ],
                              "@esbuild/android-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/android-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/darwin-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/darwin-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/freebsd-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/freebsd-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-arm": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-ia32": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-loong64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-mips64el": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-ppc64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-riscv64": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-s390x": [
                                   "0.16.12"
                              ],
                              "@esbuild/linux-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/netbsd-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/openbsd-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/sunos-x64": [
                                   "0.16.12"
                              ],
                              "@esbuild/win32-arm64": [
                                   "0.16.12"
                              ],
                              "@esbuild/win32-ia32": [
                                   "0.16.12"
                              ],
                              "@esbuild/win32-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "3c2dab15745fc060dce884dcf45da940032c6a863e05f5720266014e56c31a9b"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__path-parse__1.0.7__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:530:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__path-parse__1.0.7__links",
               "generator_name": "npm__path-parse__1.0.7__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "path-parse",
               "version": "1.0.7",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "path-parse": [
                         "1.0.7"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__path-parse__1.0.7__links",
                         "generator_name": "npm__path-parse__1.0.7__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "path-parse",
                         "version": "1.0.7",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "path-parse": [
                                   "1.0.7"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "2e5951453536d2a6c9cd99f9931ea77d682809f0eebfff405507f3ff0f894eac"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-s390x__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:245:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-s390x__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-s390x__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-s390x",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-s390x": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-s390x__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-s390x__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-s390x",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-s390x": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "252a2113593c0728fa6e1d8dd7c4ed38f49fcad71325f8bde967dba9ca77aa14"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-x64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:262:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-x64__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-x64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-x64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-x64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-x64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-x64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "fcf147041d390d7eab759a7d4b49aefce341c026c3a5db0b984ecca32980364f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_linux-riscv64__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:228:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-riscv64__0.16.12__links",
               "generator_name": "npm__at_esbuild_linux-riscv64__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-riscv64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/linux-riscv64": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-riscv64__0.16.12__links",
                         "generator_name": "npm__at_esbuild_linux-riscv64__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-riscv64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/linux-riscv64": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "c49fd163a2315ac205a1074d8648fcb71936cef3fac62b9840993912f5646b4e"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository npm__at_esbuild_android-arm__0.16.12__links instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:7:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:724:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:413:36: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_android-arm__0.16.12__links",
               "generator_name": "npm__at_esbuild_android-arm__0.16.12__links",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/android-arm",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "@esbuild/android-arm": [
                         "0.16.12"
                    ]
               },
               "lifecycle_build_target": True,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [
                    "no-sandbox"
               ],
               "npm_translate_lock_repo": "npm"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "npm__at_esbuild_android-arm__0.16.12__links",
                         "generator_name": "npm__at_esbuild_android-arm__0.16.12__links",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/android-arm",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "@esbuild/android-arm": [
                                   "0.16.12"
                              ]
                         },
                         "lifecycle_build_target": True,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [
                              "no-sandbox"
                         ],
                         "npm_translate_lock_repo": "npm"
                    },
                    "output_tree_hash": "c2a66cb22386646f4a7e7fc7247c5864ea581444951e0f177fae70119decf79d"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__vite__4.0.3 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:657:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__vite__4.0.3",
               "generator_name": "npm__vite__4.0.3",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "vite",
               "version": "4.0.3",
               "root_package": "",
               "link_packages": {
                    "": [
                         "vite"
                    ]
               },
               "extra_build_content": "",
               "integrity": "sha512-HvuNv1RdE7deIfQb8mPk51UKjqptO/4RXZ5yXSAvurd5xOckwS/gg8h9Tky3uSbnjYTgUm0hVCet1cyhKd73ZA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/vite/-/vite-4.0.3.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__vite__4.0.3",
                         "generator_name": "npm__vite__4.0.3",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "vite",
                         "version": "4.0.3",
                         "root_package": "",
                         "link_packages": {
                              "": [
                                   "vite"
                              ]
                         },
                         "extra_build_content": "",
                         "integrity": "sha512-HvuNv1RdE7deIfQb8mPk51UKjqptO/4RXZ5yXSAvurd5xOckwS/gg8h9Tky3uSbnjYTgUm0hVCet1cyhKd73ZA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/vite/-/vite-4.0.3.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "abbaf4786f1adee9cd86f01ba9cbf84513f7801280669d929354dae47fec6ed3"
               }
          ]
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "platforms",
               "path": "/home/node/.cache/bazel/_bazel_node/install/97c81a3bdd984debe0ff1b26c2dc04e0/platforms"
          },
          "native": "local_repository(name = \"platforms\", path = __embedded_dir__ + \"/\" + \"platforms\")"
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:61:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f817d64408c5484cf564d5fdc24f11c3f601835818645f6de7ab4c56eaf4056f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:45:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8e1033ec85367ff2067aa4aa175c76d9cab0f81b9d0d4f10b7743e953331b892"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:77:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b5938368c9f92a6f5045ffca11214afb8ec9256686bec9245714376aa66b67d1"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:125:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "a762e337f24b8b511c520c1101b81cc02082e3fd25e58140dfa47eb7342161ce"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:109:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4b40216fabc2f6c17810749b3bf713065a39e05ff547dac45c395be6391709af"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
          "definition_information": "Repository local_config_sh instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:515:13: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/sh/sh_configure.bzl:83:14: in sh_configure\nRepository rule sh_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/sh/sh_configure.bzl:72:28: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sh",
               "generator_name": "local_config_sh",
               "generator_function": "sh_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
                    "attributes": {
                         "name": "local_config_sh",
                         "generator_name": "local_config_sh",
                         "generator_function": "sh_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "e36855460b514225eac75f4abe2cb992c5455b7077a9028d213d269d11490744"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository local_jdk instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:31:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/local_java_repository.bzl:223:32: in local_java_repository\nRepository rule _local_java_repository_rule defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/local_java_repository.bzl:194:46: in <toplevel>\n",
          "original_attributes": {
               "name": "local_jdk",
               "generator_name": "local_jdk",
               "generator_function": "maybe",
               "generator_location": None,
               "java_home": "/home/node/.cache/bazel/_bazel_node/install/97c81a3bdd984debe0ff1b26c2dc04e0/embedded_tools/tools/jdk/nosystemjdk",
               "version": "",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "local_jdk",
                         "generator_name": "local_jdk",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "java_home": "/home/node/.cache/bazel/_bazel_node/install/97c81a3bdd984debe0ff1b26c2dc04e0/embedded_tools/tools/jdk/nosystemjdk",
                         "version": "",
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
                    },
                    "output_tree_hash": "7deac5d2bf95230828f7c2546b7befda8902258d215c97a25734dfefbe4a6348"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:157:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "383e78f7a5b828401c8b5a470bc3676797a189fe9641856f243c35e282e4384c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:173:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9cd805ebc7702094002f5373bee54fb0b9bba1ece881b83ff48c0586ddaa10d5"
               }
          ]
     },
     {
          "original_rule_class": "@rules_nodejs//nodejs/private:toolchains_repo.bzl%toolchains_repo",
          "definition_information": "Repository nodejs_toolchains instantiated at:\n  /workspaces/repro/WORKSPACE:16:27: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/rules_nodejs/nodejs/repositories.bzl:402:20: in nodejs_register_toolchains\nRepository rule toolchains_repo defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/rules_nodejs/nodejs/private/toolchains_repo.bzl:127:34: in <toplevel>\n",
          "original_attributes": {
               "name": "nodejs_toolchains",
               "generator_name": "nodejs_toolchains",
               "generator_function": "nodejs_register_toolchains",
               "generator_location": None,
               "user_node_repository_name": "nodejs"
          },
          "repositories": [
               {
                    "rule_class": "@rules_nodejs//nodejs/private:toolchains_repo.bzl%toolchains_repo",
                    "attributes": {
                         "name": "nodejs_toolchains",
                         "generator_name": "nodejs_toolchains",
                         "generator_function": "nodejs_register_toolchains",
                         "generator_location": None,
                         "user_node_repository_name": "nodejs"
                    },
                    "output_tree_hash": "9d1cdbde62627f38d6066fcb7c51f3d02c685662707e1e80e1471d6a6150a8cc"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:141:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_toolchain_config_repo",
               "generator_name": "remotejdk11_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f6c7a48666a77c098017285e46d511074ce3de7ff4e9808bc592fd49228681b2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "10df692cd4259131687761221fcb989c660f1c6e9376feba066b4fdc80bdc048"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:221:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f698cb98820064a11248ba634c70c6df5b57382ee5f8a1b589007e5b73bfc6f8"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:189:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "57763b4c6342c2729b70ccf1676a75726a4775a6e6468c86462f7247c968ecd7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:205:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8fc6087c6e654d2ff8ce626db7d0902fcf08d111f3c9f737ab19355b67d59c80"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:284:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0492adccec49cb7fafa99a8da0a43c1ecf77d62d15c2213ced41f7dd06d2a40f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:268:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7b4e118acc67f0ab2e764a34c9081459f46ecf83ede0abcb03fdbe4959b9033e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:300:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "195ddef2a390e6ceebe003a0f2ede89a2962723d5e89c88fc6f1203d84eec1c5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:252:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "78dfb0f7dab651cbc675d9dfe42e28b363ec26c3e5dc9a57b94833852f91deda"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:316:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d088fdffd2f9c3a6cdefd249980df8b6b1ac0240cb5a1e7c67655ed2f181d0fb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:348:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bb8b23eb4ea8b42cec8fd2e3752c459811f8944d1b9c66b71d53f693f71c52c7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:237:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_toolchain_config_repo",
               "generator_name": "remotejdk17_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "224a8c9f9e2f5e5cbb9efff01aa2555019675d3e1c9b93a7b4a83dfd7f5b69d5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:332:6: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_toolchain_config_repo",
               "generator_name": "remotejdk18_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0fbe406ef93edfa2dd63ecbec5eb91b55150360ebda0981365494b89015f6d4e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository local_config_cc_toolchains instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:509:13: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/cpp/cc_configure.bzl:182:27: in cc_configure\nRepository rule cc_autoconf_toolchains defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/bazel_tools/tools/cpp/cc_configure.bzl:77:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc_toolchains",
               "generator_name": "local_config_cc_toolchains",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_cc_toolchains",
                         "generator_name": "local_config_cc_toolchains",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "f95f3d84ac75b4a4d9817af803f1d998a755bd9c20c700c79fa82cb159e98cfc"
               }
          ]
     },
     {
          "original_rule_class": "@rules_nodejs//nodejs:repositories.bzl%node_repositories",
          "definition_information": "Repository nodejs_linux_amd64 instantiated at:\n  /workspaces/repro/WORKSPACE:16:27: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/rules_nodejs/nodejs/repositories.bzl:387:26: in nodejs_register_toolchains\nRepository rule node_repositories defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/rules_nodejs/nodejs/repositories.bzl:361:36: in <toplevel>\n",
          "original_attributes": {
               "name": "nodejs_linux_amd64",
               "generator_name": "nodejs_linux_amd64",
               "generator_function": "nodejs_register_toolchains",
               "generator_location": None,
               "node_version": "16.15.0",
               "platform": "linux_amd64"
          },
          "repositories": [
               {
                    "rule_class": "@rules_nodejs//nodejs:repositories.bzl%node_repositories",
                    "attributes": {
                         "name": "nodejs_linux_amd64",
                         "generator_name": "nodejs_linux_amd64",
                         "generator_function": "nodejs_register_toolchains",
                         "generator_location": None,
                         "node_version": "16.15.0",
                         "platform": "linux_amd64"
                    },
                    "output_tree_hash": "9a00225a47c5b6dc62b6de988b7970651cc076b8892818c432c834d50d653a8c"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_win32-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:364:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_win32-x64__0.16.12",
               "generator_name": "npm__at_esbuild_win32-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/win32-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-iPYKN78t3op2+erv2frW568j1q0RpqX6JOLZ7oPPaAV1VaF7dDstOrNw37PVOYoTWE11pV4A1XUitpdEFNIsPg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_win32-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_win32-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/win32-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-iPYKN78t3op2+erv2frW568j1q0RpqX6JOLZ7oPPaAV1VaF7dDstOrNw37PVOYoTWE11pV4A1XUitpdEFNIsPg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "0d165614d4497946a2f7e5f86ed34607131452b7a4f4b4cb5109f093ecd41eeb"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_android-arm64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:24:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_android-arm64__0.16.12",
               "generator_name": "npm__at_esbuild_android-arm64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/android-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-0LacmiIW+X0/LOLMZqYtZ7d4uY9fxYABAYhSSOu+OGQVBqH4N5eIYgkT7bBFnR4Nm3qo6qS3RpHKVrDASqj/uQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_android-arm64__0.16.12",
                         "generator_name": "npm__at_esbuild_android-arm64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/android-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-0LacmiIW+X0/LOLMZqYtZ7d4uY9fxYABAYhSSOu+OGQVBqH4N5eIYgkT7bBFnR4Nm3qo6qS3RpHKVrDASqj/uQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "201bb21d068a4dac68be74ef4638563420e5983833063cecc6f488e651ff4ca8"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_sunos-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:313:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_sunos-x64__0.16.12",
               "generator_name": "npm__at_esbuild_sunos-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/sunos-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-+wr1tkt1RERi+Zi/iQtkzmMH4nS8+7UIRxjcyRz7lur84wCkAITT50Olq/HiT4JN2X2bjtlOV6vt7ptW5Gw60Q==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_sunos-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_sunos-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/sunos-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-+wr1tkt1RERi+Zi/iQtkzmMH4nS8+7UIRxjcyRz7lur84wCkAITT50Olq/HiT4JN2X2bjtlOV6vt7ptW5Gw60Q==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "3b63c66b477b805be26d4492c71023036ea58b74c02def40c75be220232d3ba2"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_win32-arm64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:330:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_win32-arm64__0.16.12",
               "generator_name": "npm__at_esbuild_win32-arm64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/win32-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-XEjeUSHmjsAOJk8+pXJu9pFY2O5KKQbHXZWQylJzQuIBeiGrpMeq9sTVrHefHxMOyxUgoKQTcaTS+VK/K5SviA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_win32-arm64__0.16.12",
                         "generator_name": "npm__at_esbuild_win32-arm64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/win32-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-XEjeUSHmjsAOJk8+pXJu9pFY2O5KKQbHXZWQylJzQuIBeiGrpMeq9sTVrHefHxMOyxUgoKQTcaTS+VK/K5SviA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "57be17b6acc8720e65872a388c1b84ecc3ca41786091d75f977161ef0ed15a4f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__esbuild__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:381:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__esbuild__0.16.12",
               "generator_name": "npm__esbuild__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "esbuild",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-eq5KcuXajf2OmivCl4e89AD3j8fbV+UTE9vczEzq5haA07U9oOTzBWlh3+6ZdjJR7Rz2QfWZ2uxZyhZxBgJ4+g==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/esbuild/-/esbuild-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__esbuild__0.16.12",
                         "generator_name": "npm__esbuild__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "esbuild",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-eq5KcuXajf2OmivCl4e89AD3j8fbV+UTE9vczEzq5haA07U9oOTzBWlh3+6ZdjJR7Rz2QfWZ2uxZyhZxBgJ4+g==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/esbuild/-/esbuild-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "f5cf19772dc176c383a1273db43cd1216a976f519a2727db568205c31c262f19"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__fsevents__2.3.2 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:444:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__fsevents__2.3.2",
               "generator_name": "npm__fsevents__2.3.2",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "fsevents",
               "version": "2.3.2",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-xiqMQR4xAeHTuB9uWm+fFRcIOgKBMiOBP+eXiyT7jsgVCq1bkVygt00oASowB7EdtpOHaaPgKt812P9ab+DDKA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.2.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__fsevents__2.3.2",
                         "generator_name": "npm__fsevents__2.3.2",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "fsevents",
                         "version": "2.3.2",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-xiqMQR4xAeHTuB9uWm+fFRcIOgKBMiOBP+eXiyT7jsgVCq1bkVygt00oASowB7EdtpOHaaPgKt812P9ab+DDKA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.2.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "34fdc951f76f1e94a694905422b52f419e2842e389a3f132047e86b8676d752c"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_android-arm__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:7:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_android-arm__0.16.12",
               "generator_name": "npm__at_esbuild_android-arm__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/android-arm",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-CTWgMJtpCyCltrvipZrrcjjRu+rzm6pf9V8muCsJqtKujR3kPmU4ffbckvugNNaRmhxAF1ZI3J+0FUIFLFg8KA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_android-arm__0.16.12",
                         "generator_name": "npm__at_esbuild_android-arm__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/android-arm",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-CTWgMJtpCyCltrvipZrrcjjRu+rzm6pf9V8muCsJqtKujR3kPmU4ffbckvugNNaRmhxAF1ZI3J+0FUIFLFg8KA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "6b2f24ee3eef7a4280c0e9cc9d7eb835677aa9cadb9d30fed9b25f48a6397c12"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_openbsd-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:296:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_openbsd-x64__0.16.12",
               "generator_name": "npm__at_esbuild_openbsd-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/openbsd-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-PAonw4LqIybwn2/vJujhbg1N9W2W8lw9RtXIvvZoyzoA/4rA4CpiuahVbASmQohiytRsixbNoIOUSjRygKXpyA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_openbsd-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_openbsd-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/openbsd-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-PAonw4LqIybwn2/vJujhbg1N9W2W8lw9RtXIvvZoyzoA/4rA4CpiuahVbASmQohiytRsixbNoIOUSjRygKXpyA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "19965ba8929cd83f83f9b0a450e4dafd77d00bf5b3973422bedff0b36e5cd5f5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_win32-ia32__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:347:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_win32-ia32__0.16.12",
               "generator_name": "npm__at_esbuild_win32-ia32__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/win32-ia32",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-eRKPM7e0IecUAUYr2alW7JGDejrFJXmpjt4MlfonmQ5Rz9HWpKFGCjuuIRgKO7W9C/CWVFXdJ2GjddsBXqQI4A==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_win32-ia32__0.16.12",
                         "generator_name": "npm__at_esbuild_win32-ia32__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/win32-ia32",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-eRKPM7e0IecUAUYr2alW7JGDejrFJXmpjt4MlfonmQ5Rz9HWpKFGCjuuIRgKO7W9C/CWVFXdJ2GjddsBXqQI4A==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "a718ed16a2f72a17cc7a06bcd72c832b18c44f59d4bf5337fad62df9c6d82a89"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:262:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-x64__0.16.12",
               "generator_name": "npm__at_esbuild_linux-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-e8YA7GQGLWhvakBecLptUiKxOk4E/EPtSckS1i0MGYctW8ouvNUoh7xnU15PGO2jz7BYl8q1R6g0gE5HFtzpqQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-e8YA7GQGLWhvakBecLptUiKxOk4E/EPtSckS1i0MGYctW8ouvNUoh7xnU15PGO2jz7BYl8q1R6g0gE5HFtzpqQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "095472556dcbb49ed50aa735e02942954ad60abae5ed5c44a78876afb8cc444d"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_freebsd-arm64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:92:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_freebsd-arm64__0.16.12",
               "generator_name": "npm__at_esbuild_freebsd-arm64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/freebsd-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-AMdK2gA9EU83ccXCWS1B/KcWYZCj4P3vDofZZkl/F/sBv/fphi2oUqUTox/g5GMcIxk8CF1CVYTC82+iBSyiUg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_freebsd-arm64__0.16.12",
                         "generator_name": "npm__at_esbuild_freebsd-arm64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/freebsd-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-AMdK2gA9EU83ccXCWS1B/KcWYZCj4P3vDofZZkl/F/sBv/fphi2oUqUTox/g5GMcIxk8CF1CVYTC82+iBSyiUg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "db97d25054138bace3bf008571320a0c86ba2e4fd4645114fe3ef2ef20e2be36"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__resolve__1.22.1 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:583:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__resolve__1.22.1",
               "generator_name": "npm__resolve__1.22.1",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "resolve",
               "version": "1.22.1",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-nBpuuYuY5jFsli/JIs1oldw6fOQCBioohqWZg/2hiaOybXOft4lonv85uDOKXdf8rhyK159cxU5cDcK/NKk8zw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/resolve/-/resolve-1.22.1.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__resolve__1.22.1",
                         "generator_name": "npm__resolve__1.22.1",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "resolve",
                         "version": "1.22.1",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-nBpuuYuY5jFsli/JIs1oldw6fOQCBioohqWZg/2hiaOybXOft4lonv85uDOKXdf8rhyK159cxU5cDcK/NKk8zw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/resolve/-/resolve-1.22.1.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "9ecf538d0cbf30fae3215f8c74a6cd7c6c6de247216147e8335522e115adf3cb"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_netbsd-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:279:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_netbsd-x64__0.16.12",
               "generator_name": "npm__at_esbuild_netbsd-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/netbsd-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-z2+kUxmOqBS+6SRVd57iOLIHE8oGOoEnGVAmwjm2aENSP35HPS+5cK+FL1l+rhrsJOFIPrNHqDUNechpuG96Sg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_netbsd-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_netbsd-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/netbsd-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-z2+kUxmOqBS+6SRVd57iOLIHE8oGOoEnGVAmwjm2aENSP35HPS+5cK+FL1l+rhrsJOFIPrNHqDUNechpuG96Sg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "63db6426ca513902e0404f11fa12a332c0bc51c743ce8958b301d35e6100a040"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_android-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:41:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_android-x64__0.16.12",
               "generator_name": "npm__at_esbuild_android-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/android-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-sS5CR3XBKQXYpSGMM28VuiUnbX83Z+aWPZzClW+OB2JquKqxoiwdqucJ5qvXS8pM6Up3RtJfDnRQZkz3en2z5g==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_android-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_android-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/android-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-sS5CR3XBKQXYpSGMM28VuiUnbX83Z+aWPZzClW+OB2JquKqxoiwdqucJ5qvXS8pM6Up3RtJfDnRQZkz3en2z5g==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "69c6e247a35169cfe0ccc5b788aa0ebac8236b0489fc4b74b6c8d78821c0bfc5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__path-parse__1.0.7 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:530:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__path-parse__1.0.7",
               "generator_name": "npm__path-parse__1.0.7",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "path-parse",
               "version": "1.0.7",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__path-parse__1.0.7",
                         "generator_name": "npm__path-parse__1.0.7",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "path-parse",
                         "version": "1.0.7",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "0181352df8e58c4d05ad70d4d3883bdba43f085de73e8c116c6c57356fe8aa91"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__rollup__3.9.1 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:608:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__rollup__3.9.1",
               "generator_name": "npm__rollup__3.9.1",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "rollup",
               "version": "3.9.1",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-GswCYHXftN8ZKGVgQhTFUJB/NBXxrRGgO2NCy6E8s1rwEJ4Q9/VttNqcYfEvx4dTo4j58YqdC3OVztPzlKSX8w==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/rollup/-/rollup-3.9.1.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__rollup__3.9.1",
                         "generator_name": "npm__rollup__3.9.1",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "rollup",
                         "version": "3.9.1",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-GswCYHXftN8ZKGVgQhTFUJB/NBXxrRGgO2NCy6E8s1rwEJ4Q9/VttNqcYfEvx4dTo4j58YqdC3OVztPzlKSX8w==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/rollup/-/rollup-3.9.1.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "b69d44d844115c22e26c3a8db4f5c0d8f12a7cd657e47e01310269e3373256c1"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-ppc64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:211:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-ppc64__0.16.12",
               "generator_name": "npm__at_esbuild_linux-ppc64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-ppc64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-/C8OFXExoMmvTDIOAM54AhtmmuDHKoedUd0Otpfw3+AuuVGemA1nQK99oN909uZbLEU6Bi+7JheFMG3xGfZluQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-ppc64__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-ppc64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-ppc64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-/C8OFXExoMmvTDIOAM54AhtmmuDHKoedUd0Otpfw3+AuuVGemA1nQK99oN909uZbLEU6Bi+7JheFMG3xGfZluQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "2b968f02b929e69e4f2f5f1e3923dd4f419dcf3acc1b969196601479f299d9e9"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-riscv64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:228:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-riscv64__0.16.12",
               "generator_name": "npm__at_esbuild_linux-riscv64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-riscv64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-qeouyyc8kAGV6Ni6Isz8hUsKMr00EHgVwUKWNp1r4l88fHEoNTDB8mmestvykW6MrstoGI7g2EAsgr0nxmuGYg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-riscv64__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-riscv64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-riscv64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-qeouyyc8kAGV6Ni6Isz8hUsKMr00EHgVwUKWNp1r4l88fHEoNTDB8mmestvykW6MrstoGI7g2EAsgr0nxmuGYg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "a1d4be54880dd28d67d0c279dcea232558862369a5a04cf99f8b3ea337410a7e"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-s390x__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:245:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-s390x__0.16.12",
               "generator_name": "npm__at_esbuild_linux-s390x__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-s390x",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-s9AyI/5vz1U4NNqnacEGFElqwnHusWa81pskAf8JNDM2eb6b2E6PpBmT8RzeZv6/TxE6/TADn2g9bb0jOUmXwQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-s390x__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-s390x__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-s390x",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-s9AyI/5vz1U4NNqnacEGFElqwnHusWa81pskAf8JNDM2eb6b2E6PpBmT8RzeZv6/TxE6/TADn2g9bb0jOUmXwQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "dbc6c77e7fab4e70578ed301fb2b699fa145a03e6184f2b3550e7d687b90cb44"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_darwin-arm64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:58:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_darwin-arm64__0.16.12",
               "generator_name": "npm__at_esbuild_darwin-arm64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/darwin-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-Dpe5hOAQiQRH20YkFAg+wOpcd4PEuXud+aGgKBQa/VriPJA8zuVlgCOSTwna1CgYl05lf6o5els4dtuyk1qJxQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_darwin-arm64__0.16.12",
                         "generator_name": "npm__at_esbuild_darwin-arm64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/darwin-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-Dpe5hOAQiQRH20YkFAg+wOpcd4PEuXud+aGgKBQa/VriPJA8zuVlgCOSTwna1CgYl05lf6o5els4dtuyk1qJxQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "bc1f2389b8d547f52e41155123b2fd1867bf0fc944c9b32ac6d781cb563f804e"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__function-bind__1.1.1 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:461:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__function-bind__1.1.1",
               "generator_name": "npm__function-bind__1.1.1",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "function-bind",
               "version": "1.1.1",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-yIovAzMX49sF8Yl58fSCWJ5svSLuaibPxXQJFLmBObTuCr0Mf1KiPopGM9NiFjiYBCbfaa2Fh6breQ6ANVTI0A==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__function-bind__1.1.1",
                         "generator_name": "npm__function-bind__1.1.1",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "function-bind",
                         "version": "1.1.1",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-yIovAzMX49sF8Yl58fSCWJ5svSLuaibPxXQJFLmBObTuCr0Mf1KiPopGM9NiFjiYBCbfaa2Fh6breQ6ANVTI0A==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "5a806dd5b9c725a1ca8780407797af3c2aa25ad747e1fb3390cac6cf8ee1efd5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__nanoid__3.3.4 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:515:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__nanoid__3.3.4",
               "generator_name": "npm__nanoid__3.3.4",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "nanoid",
               "version": "3.3.4",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-MqBkQh/OHTS2egovRtLk45wEyNXwF+cokD+1YPf9u5VfJiRdAiRwB2froX5Co9Rh20xs4siNPm8naNotSD6RBw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.4.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__nanoid__3.3.4",
                         "generator_name": "npm__nanoid__3.3.4",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "nanoid",
                         "version": "3.3.4",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-MqBkQh/OHTS2egovRtLk45wEyNXwF+cokD+1YPf9u5VfJiRdAiRwB2froX5Co9Rh20xs4siNPm8naNotSD6RBw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.4.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "0b142a25271d01ada34077c3fb84837d18c00ca78433a39fa1a9df26d9d01895"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_darwin-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:75:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_darwin-x64__0.16.12",
               "generator_name": "npm__at_esbuild_darwin-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/darwin-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-ApGRA6X5txIcxV0095X4e4KKv87HAEXfuDRcGTniDWUUN+qPia8sl/BqG/0IomytQWajnUn4C7TOwHduk/FXBQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_darwin-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_darwin-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/darwin-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-ApGRA6X5txIcxV0095X4e4KKv87HAEXfuDRcGTniDWUUN+qPia8sl/BqG/0IomytQWajnUn4C7TOwHduk/FXBQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "dace2ce166b203d9bbe770a3cccef969d737a1c12ea6bf229e4497796de4a539"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__picocolors__1.0.0 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:545:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__picocolors__1.0.0",
               "generator_name": "npm__picocolors__1.0.0",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "picocolors",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__picocolors__1.0.0",
                         "generator_name": "npm__picocolors__1.0.0",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "picocolors",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "7995bed5b84cb653f0045da90711c98bebdd9d76bf7d036b2081a80aa468764f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__is-core-module__2.11.0 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:495:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__is-core-module__2.11.0",
               "generator_name": "npm__is-core-module__2.11.0",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "is-core-module",
               "version": "2.11.0",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-RRjxlvLDkD1YJwDbroBHMb+cukurkDWNyHx7D3oNB5x9rb5ogcksMC5wHCadcXoo67gVr/+3GFySh3134zi6rw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.11.0.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__is-core-module__2.11.0",
                         "generator_name": "npm__is-core-module__2.11.0",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "is-core-module",
                         "version": "2.11.0",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-RRjxlvLDkD1YJwDbroBHMb+cukurkDWNyHx7D3oNB5x9rb5ogcksMC5wHCadcXoo67gVr/+3GFySh3134zi6rw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.11.0.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "f5fc36326aa681cba46940844b2c6f48b47f3a7f01bf73680389f26cfcba6c91"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__source-map-js__1.0.2 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:627:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__source-map-js__1.0.2",
               "generator_name": "npm__source-map-js__1.0.2",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "source-map-js",
               "version": "1.0.2",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-R0XvVJ9WusLiqTCEiGCmICCMplcCkIwwR11mOSD9CR5u+IXYdiseeEuXCVAjS54zqwkLcPNnmU4OeJ6tUrWhDw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.0.2.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__source-map-js__1.0.2",
                         "generator_name": "npm__source-map-js__1.0.2",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "source-map-js",
                         "version": "1.0.2",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-R0XvVJ9WusLiqTCEiGCmICCMplcCkIwwR11mOSD9CR5u+IXYdiseeEuXCVAjS54zqwkLcPNnmU4OeJ6tUrWhDw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.0.2.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "21c733a3964bbba27d8fcee3030fb64f9cb14554397efbf73e34bad5a4e81d11"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_freebsd-x64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:109:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_freebsd-x64__0.16.12",
               "generator_name": "npm__at_esbuild_freebsd-x64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/freebsd-x64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-KUKB9w8G/xaAbD39t6gnRBuhQ8vIYYlxGT2I+mT6UGRnCGRr1+ePFIGBQmf5V16nxylgUuuWVW1zU2ktKkf6WQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_freebsd-x64__0.16.12",
                         "generator_name": "npm__at_esbuild_freebsd-x64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/freebsd-x64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-KUKB9w8G/xaAbD39t6gnRBuhQ8vIYYlxGT2I+mT6UGRnCGRr1+ePFIGBQmf5V16nxylgUuuWVW1zU2ktKkf6WQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "03abe4e7ffedf7ebef86fb7f577492d0f0c5accad426fa619e118783fdc4c87f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__supports-preserve-symlinks-flag__1.0.0 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:642:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__supports-preserve-symlinks-flag__1.0.0",
               "generator_name": "npm__supports-preserve-symlinks-flag__1.0.0",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "supports-preserve-symlinks-flag",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__supports-preserve-symlinks-flag__1.0.0",
                         "generator_name": "npm__supports-preserve-symlinks-flag__1.0.0",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "supports-preserve-symlinks-flag",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "7a5c5a6ac53a8267384d8fc28f3b7a1c43da8965eae9a1776912c9432cf6ed51"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__has__1.0.3 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:476:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__has__1.0.3",
               "generator_name": "npm__has__1.0.3",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "has",
               "version": "1.0.3",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-f2dvO0VU6Oej7RkWJGrehjbzMAjFp5/VKPp5tTpWIV4JHHZK1/BxbFRtf/siA2SWTe09caDmVtYYzWEIbBS4zw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/has/-/has-1.0.3.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__has__1.0.3",
                         "generator_name": "npm__has__1.0.3",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "has",
                         "version": "1.0.3",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-f2dvO0VU6Oej7RkWJGrehjbzMAjFp5/VKPp5tTpWIV4JHHZK1/BxbFRtf/siA2SWTe09caDmVtYYzWEIbBS4zw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/has/-/has-1.0.3.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "d9295447f4bd33432dc8cd1326bf3d37fbebd31f6331b16d9a4c5c7bc9fa4e42"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-mips64el__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:194:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-mips64el__0.16.12",
               "generator_name": "npm__at_esbuild_linux-mips64el__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-mips64el",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-zI1cNgHa3Gol+vPYjIYHzKhU6qMyOQrvZ82REr5Fv7rlh5PG6SkkuCoH7IryPqR+BK2c/7oISGsvPJPGnO2bHQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-mips64el__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-mips64el__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-mips64el",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-zI1cNgHa3Gol+vPYjIYHzKhU6qMyOQrvZ82REr5Fv7rlh5PG6SkkuCoH7IryPqR+BK2c/7oISGsvPJPGnO2bHQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "efd4a145a618ba5b5092ac571a7a66e40ed5f5c6fd29fc56d7b33b623f91194b"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-arm64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:143:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-arm64__0.16.12",
               "generator_name": "npm__at_esbuild_linux-arm64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-arm64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-29HXMLpLklDfmw7T2buGqq3HImSUaZ1ArmrPOMaNiZZQptOSZs32SQtOHEl8xWX5vfdwZqrBfNf8Te4nArVzKQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-arm64__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-arm64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-arm64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-29HXMLpLklDfmw7T2buGqq3HImSUaZ1ArmrPOMaNiZZQptOSZs32SQtOHEl8xWX5vfdwZqrBfNf8Te4nArVzKQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "0a14bfc0151797594654471b2a530d0811e2e9bc466b90e1a86727a3eace6eb2"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-loong64__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:177:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-loong64__0.16.12",
               "generator_name": "npm__at_esbuild_linux-loong64__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-loong64",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-xTGzVPqm6WKfCC0iuj1fryIWr1NWEM8DMhAIo+4rFgUtwy/lfHl+Obvus4oddzRDbBetLLmojfVZGmt/g/g+Rw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-loong64__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-loong64__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-loong64",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-xTGzVPqm6WKfCC0iuj1fryIWr1NWEM8DMhAIo+4rFgUtwy/lfHl+Obvus4oddzRDbBetLLmojfVZGmt/g/g+Rw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "698bd4e5a7c8b246d9e7106773b9e34e104a55e042bd49686e6c81a67bb5bcc3"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__postcss__8.4.20 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:560:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__postcss__8.4.20",
               "generator_name": "npm__postcss__8.4.20",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "postcss",
               "version": "8.4.20",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-6Q04AXR1212bXr5fh03u8aAwbLxAQNGQ/Q1LNa0VfOI06ZAlhPHtQvE4OIdpj4kLThXilalPnmDSOD65DcHt+g==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/postcss/-/postcss-8.4.20.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__postcss__8.4.20",
                         "generator_name": "npm__postcss__8.4.20",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "postcss",
                         "version": "8.4.20",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-6Q04AXR1212bXr5fh03u8aAwbLxAQNGQ/Q1LNa0VfOI06ZAlhPHtQvE4OIdpj4kLThXilalPnmDSOD65DcHt+g==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/postcss/-/postcss-8.4.20.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "655b1ed54243ca8a545bda4fffac13177e8aa840e7649d46ea5cf81c3239099a"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-arm__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:126:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-arm__0.16.12",
               "generator_name": "npm__at_esbuild_linux-arm__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-arm",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-vhDdIv6z4eL0FJyNVfdr3C/vdd/Wc6h1683GJsFoJzfKb92dU/v88FhWdigg0i6+3TsbSDeWbsPUXb4dif2abg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-arm__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-arm__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-arm",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-vhDdIv6z4eL0FJyNVfdr3C/vdd/Wc6h1683GJsFoJzfKb92dU/v88FhWdigg0i6+3TsbSDeWbsPUXb4dif2abg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "ace75710fe236809120a45dd18a52657f1353d9749bde7d195d7941bfec60d7f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository npm__at_esbuild_linux-ia32__0.16.12 instantiated at:\n  /workspaces/repro/WORKSPACE:31:17: in <toplevel>\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/npm/repositories.bzl:160:15: in npm_repositories\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:691:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/node/.cache/bazel/_bazel_node/bd31105343571d27cb38c68d58484397/external/aspect_rules_js/npm/npm_import.bzl:418:30: in <toplevel>\n",
          "original_attributes": {
               "name": "npm__at_esbuild_linux-ia32__0.16.12",
               "generator_name": "npm__at_esbuild_linux-ia32__0.16.12",
               "generator_function": "npm_repositories",
               "generator_location": None,
               "package": "@esbuild/linux-ia32",
               "version": "0.16.12",
               "root_package": "",
               "link_packages": {},
               "extra_build_content": "",
               "integrity": "sha512-JFDuNDTTfgD1LJg7wHA42o2uAO/9VzHYK0leAVnCQE/FdMB599YMH73ux+nS0xGr79pv/BK+hrmdRin3iLgQjg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "lifecycle_hooks": [
                    "preinstall",
                    "install",
                    "postinstall"
               ],
               "custom_postinstall": "",
               "link_workspace": "",
               "url": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.16.12.tgz",
               "commit": "",
               "npm_auth": "",
               "npm_auth_basic": "",
               "npm_auth_username": "",
               "npm_auth_password": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "npm__at_esbuild_linux-ia32__0.16.12",
                         "generator_name": "npm__at_esbuild_linux-ia32__0.16.12",
                         "generator_function": "npm_repositories",
                         "generator_location": None,
                         "package": "@esbuild/linux-ia32",
                         "version": "0.16.12",
                         "root_package": "",
                         "link_packages": {},
                         "extra_build_content": "",
                         "integrity": "sha512-JFDuNDTTfgD1LJg7wHA42o2uAO/9VzHYK0leAVnCQE/FdMB599YMH73ux+nS0xGr79pv/BK+hrmdRin3iLgQjg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "lifecycle_hooks": [
                              "preinstall",
                              "install",
                              "postinstall"
                         ],
                         "custom_postinstall": "",
                         "link_workspace": "",
                         "url": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.16.12.tgz",
                         "commit": "",
                         "npm_auth": "",
                         "npm_auth_basic": "",
                         "npm_auth_username": "",
                         "npm_auth_password": ""
                    },
                    "output_tree_hash": "afdc6c11114aef7ecdc4e61cd45b1a9838930713aaab4173756c0f1abc75f588"
               }
          ]
     }
]